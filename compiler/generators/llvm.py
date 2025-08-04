from typing import Optional
from llvmlite import ir
from vast import *
from compiler.meta import *

# Metadata keys
LLVM_OBJECT = "GEN__LLVM__OBJECT"
LLVM_START_BLOCK = "GEN__LLVM__START_BLOCK"
LLVM_END_BLOCK = "GEN__LLVM__END_BLOCK"

class LLVMGeneratorContext:
    module: Optional[ir.Module] = None
    current_function: Optional[ir.Function] = None
    current_builder: Optional[ir.IRBuilder] = None
    simple_block_labels: dict[str, int]

    def __init__(self):
        self.simple_block_labels = {}
        self.module = None
        self.current_function = None
        self.current_builder = None

    def default_file_name(self, vmodule: VModule) -> str:
        return f"{vmodule.name if vmodule.name else 'module'}.ll"

    def enter_function(self, function: ir.Function):
        ctx = self
        class FunctionContext:
            def __enter__(self):
                self.prev_function = ctx.current_function
                ctx.current_function = function
                return ctx.current_function

            def __exit__(self, exc_type, exc_value, traceback):
                ctx.current_function = self.prev_function
        return FunctionContext()

    def set_builder(self, builder: ir.IRBuilder):
        # This needs to affect the instructions after a VBlock, since LLVM simple blocks are all flat in the function.
        # But, this won't work if I were to make a function
        self.current_builder = builder

    def request_label(self, label: str):
        if label not in self.simple_block_labels:
            self.simple_block_labels[label] = 0
        else:
            self.simple_block_labels[label] += 1
        return f"{label}__{self.simple_block_labels[label]}"


#end LLVMGeneratorContext


def generate(node: VASTNode, ctx: LLVMGeneratorContext, **kwargs) -> ir.Value | ir.Type | ir.Module | ir.Function:
    match node:
        case VModule():
            vmodule: VModule = node
            llvm_module = ir.Module(name="mod") # TODO: get module name from filename?
            ctx.module = llvm_module

            for item in vmodule.items:
                generate(item, ctx, current_module=llvm_module)

            vmodule.meta[LLVM_OBJECT] = llvm_module
            return llvm_module
        #end VModule
        case VFunction():
            vfunction: VFunction = node
            if LLVM_OBJECT in vfunction.meta:
                return vfunction.meta[LLVM_OBJECT]

            # TODO - change into generate(vfunction.signature, ctx), when signature objects are implemented
            llvm_function_type = ir.FunctionType(generate(vfunction.return_type, ctx),
                                                 args=(*(generate(arg.type, ctx) for arg in vfunction.targets),
                                                   *(generate(arg.type, ctx) for arg in vfunction.args)),
                                                 )
            if vfunction.extern_name:
                name = vfunction.extern_name
            else:
                name = vfunction.name # TODO: use possibly mangled name
            llvm_function = ir.Function(ctx.module, llvm_function_type, name=name)
            # TODO - Naming arguments
            if vfunction.body:
                with ctx.enter_function(llvm_function):
                    ctx.set_builder(ir.IRBuilder(llvm_function.append_basic_block("entry")))
                    # TODO - Make arguments into variables for correctness
                    for item in vfunction.body.body: # Ok, this looks ridiculous. Maybe I should rename the field in VBlock?
                        generate(item, ctx)
            else:
                assert vfunction.extern_kind != VFunction.ExternKind.NOT_EXTERN
                # Make it a declaration
                llvm_function.blocks = []
            vfunction.meta[LLVM_OBJECT] = llvm_function
            return llvm_function
        #end VFunction
        case VBlock():
            # This case is only intended for standalone VBlocks
            vblock: VBlock = node
            current_function: ir.Function = ctx.current_function
            if current_function is None:
                raise ValueError("Current function must be provided for block generation.")

            final_label: str = ctx.request_label(vblock.label if vblock.label else "procedure")
            llvm_start_block = current_function.append_basic_block(f"{final_label}__start")
            llvm_end_block = current_function.append_basic_block(f"{final_label}__end")
            vblock.meta[LLVM_START_BLOCK] = llvm_start_block
            vblock.meta[LLVM_END_BLOCK] = llvm_end_block

            ctx.set_builder(ir.IRBuilder(llvm_start_block))
            for statement in vblock.body:
                generate(statement, ctx)
            ctx.set_builder(ir.IRBuilder(llvm_end_block))
            return llvm_start_block
        #end VBlock
        case VCall():
            vcall: VCall = node
            builder: ir.IRBuilder = ctx.current_builder
            if builder is None:
                raise ValueError("Builder must be provided for call generation.")

            vfunction: VFunction = vcall.meta[RESOLVES_TO]

            args = (*(generate(target, ctx) for target in vcall.targets), *(generate(arg, ctx) for arg in vcall.args))

            # TODO - Inlining
            function_to_call: ir.Function = generate(vfunction, ctx)
            call_instruction = builder.call(function_to_call, args, cconv=function_to_call.calling_convention)

            vcall.meta[LLVM_OBJECT] = call_instruction
            return call_instruction
        #end VCall
        case VReturn():
            vreturn: VReturn = node
            builder: ir.IRBuilder = ctx.current_builder
            if builder is None:
                raise ValueError("Builder must be provided for return generation.")
            if len(vreturn.values) == 1:
                return_value = generate(vreturn.values[0], ctx)
                if not isinstance(return_value, ir.Value):
                    raise ValueError("Return value must be an LLVM Value.")
                ret = builder.ret(return_value)
            elif len(vreturn.values) > 1:
                raise NotImplementedError("Tuple returns are not implemented yet.")
            else:
                ret = builder.ret_void()
            return ret
        #end VReturn
        case VIntLiteral():
            vliteral: VIntLiteral = node
            return ir.Constant(generate(vliteral.type, ctx), vliteral.value)
        #end VIntLiteral
        case VStringLiteral():
            vliteral: VStringLiteral = node
            # TODO - register all the created strings for reuse in the ctx
            # Have to create a global string constant
            llvm_string_type = ir.ArrayType(ir.IntType(8), len(vliteral.value.encode('utf-8')) + 1) # +1 for null terminator
            str_constant = ir.GlobalVariable(module=ctx.module, typ=llvm_string_type,
                                          name=ctx.request_label("__STRING_LITERAL")) # I guess I can reuse the function I made for block labels?
            str_constant.initializer = ir.Constant(llvm_string_type, bytearray(vliteral.value.encode('utf-8') + b'\x00'))
            str_constant.linkage = 'private'
            vliteral.meta[LLVM_OBJECT] = str_constant
            return ctx.current_builder.bitcast(str_constant, ir.PointerType(ir.IntType(8))) # Cast to pointer to char
        #end VStringLiteral
        case VNameAccess():
            vnameaccess: VNameAccess = node
            raise NotImplementedError() # TODO - this might be in either a context of an expression or a function call?
            # Maybe it'll be better if expressions have a separate generate function?
            return vnameaccess.meta[RESOLVES_TO]
        #end VNameAccess
        case VFundamentalType():
            vfundamentaltype: VFundamentalType = node
            if LLVM_OBJECT in vfundamentaltype.meta:
                return vfundamentaltype.meta[LLVM_OBJECT]
            if vfundamentaltype.t == VFundamentalType.T.INT or vfundamentaltype.t == VFundamentalType.T.UINT:
                assert(vfundamentaltype.bits != VFundamentalType.Bits.UNSPECIFIED)
                llvm_type = ir.IntType(vfundamentaltype.bits)
            elif vfundamentaltype.t == VFundamentalType.T.FLOAT:
                match vfundamentaltype.bits:
                    case VFundamentalType.Bits.b32:
                        llvm_type = ir.FloatType()
                    case VFundamentalType.Bits.b64:
                        llvm_type = ir.DoubleType()
                    case _:
                        raise NotImplementedError(f"Unsupported bit number for floats: {vfundamentaltype.bits}")
            else:
                raise NotImplementedError(f"Unknown VFundamentalType: {vfundamentaltype.t}")
            vfundamentaltype.meta[LLVM_OBJECT] = llvm_type
            return llvm_type
        #end VFundamentalType
        case VNamedType():
            vnamedtype: VNamedType = node
            if LLVM_OBJECT in vnamedtype.meta:
                return vnamedtype.meta[LLVM_OBJECT]
            llvm_type = generate(vnamedtype.meta[RESOLVES_TO], ctx)
            vnamedtype.meta[LLVM_OBJECT] = llvm_type
            return llvm_type
        #end VNamedType
        case VPointerType():
            vpointer: VPointerType = node
            if LLVM_OBJECT in vpointer.meta:
                return vpointer.meta[LLVM_OBJECT]
            llvm_pointer = ir.PointerType(generate(vpointer.to, ctx))
            return llvm_pointer
        #end VPointerType
        case _:
            raise NotImplementedError(f"LLVM code generation for {node.__class__.__name__} not implemented yet.")
        #end _
    #end match
#end generate
