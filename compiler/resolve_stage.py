from unittest import case

from common import CompileError
from .contexts import CompileContext

from common.errors import ObjectAlreadyDefinedException
from vast import *
from vast.scope import Scope
from .meta import *


def register_module(root: VModule, ctx: CompileContext):
    """
    Register names in the module's scope.
    Uses a breadth-first search to register names in the global module's scope,
    so ex. functions can be used before they are defined.
    """
    with ctx.enter_scope(root.scope) as current_scope:
        # Step 1: Register global names in the module's scope
        for item in root.items:
            match item:
                # TODO - Imports
                case VSection():
                    # VSections are intended to be used for grouping items in the module,
                    # so their items will be registered in the module's scope.
                    raise NotImplementedError("VSection not implemented yet.")
                case ScopeItem():
                    # Register the item in the module's scope
                    current_scope.define(item.name, item)
                    item.meta[MODULE_LEVEL] = True
                case _:
                    # We may have other unnamed types of items in the module in the future, that we may want to ignore
                    # For now, we will just raise an error if we encounter an unexpected item type.
                    raise TypeError(f"Unexpected item type: {type(item)}")
        # Step 2
        for item in root.items:
            resolve(item, ctx)

    #end with
#end module_register


def define_if_local(node: VASTNode, ctx: CompileContext):
    """
    Only use for nodes that can be directly in the module!
    :param node:
    :param ctx:
    :return:
    """
    if node.meta.get(MODULE_LEVEL, False):
        # This is a module-level item, so it has already been defined
        return
    ctx.current_scope.define(node.name, node)
#end define_if_local


def resolve(node, ctx: CompileContext):
    """
    First major pass of the compiler.
    This pass will register names in the module's scope and resolve the names to the ScopeItems they refer to.
    Also, probably do type checking.
    """
    match node:
        case VModule():
            # Might happen in the future with imports, then I'll need to handle it
            raise NotImplementedError("Module handling in resolve() not implemented yet.")
        case VSection():
            # This will just resolve the subitems in the section
            raise NotImplementedError("Section handling in resolve() not implemented yet.")
        ## Module items, declarations ##
        case VTypeDeclaration():
            decl: VTypeDeclaration = node
            # Resolve the type inside the declaration
            with ctx.enter_parenthood(decl): # To detect recursive type declarations
                resolve(decl.type, ctx)

            define_if_local(decl, ctx)
        #end VTypeDeclaration
        case VFunction():
            func: VFunction = node

            # Resolve the function signature
            resolve(func.return_type, ctx)
            with ctx.enter_scope(func.body.scope), ctx.enter_parenthood(func):
                for target in func.targets:
                    resolve(target, ctx)
                for arg in func.args:
                    resolve(arg, ctx)
                # TODO - generate the function signature object

            # Body's resolve will also enter its scope, so we need to exit it here
            resolve(func.body, ctx)
            # Register the function in the current scope
            define_if_local(func, ctx)

        #end VFunction
        case VVariable():
            var: VVariable = node

            if var.init_value is not None:
                with ctx.enter_parenthood(var): # Might actually be unnecessary now, since registering the name of variable after avoids recursion? ... ok, global variables.
                    resolve(var.init_value, ctx)

            # TODO - implement type inference here, once it's also in grammar?
            resolve(var.type, ctx)

            define_if_local(var, ctx)
        #end VVariable
        # Statements
        case VCall():
            call: VCall = node
            with ctx.enter_parenthood(call):
                for target in call.targets:
                    resolve(target, ctx)
                for arg in call.args:
                    resolve(arg, ctx)
                # TODO - Construct a function signature?
                # Temp implementation - does not account for function overloading
                resolve(call.func, ctx)
                assert(isinstance(call.func, VNameAccess)) # Temp, until I implement namespaces
                call.meta[RESOLVES_TO] = call.func.meta[RESOLVES_TO]
        #end VCall
        case VReturn():
            # TODO
            pass
        #end VReturn
        case VNameAccess():
            access: VNameAccess = node
            resolves_to = ctx.current_scope.lookup(access.name)
            if resolves_to is None:
                raise CompileError(f"{access.meta["location"]} Undefined name {access.name}") # This should be a critical error
            if ctx.is_illegally_recursive(resolves_to):
                raise CompileError(f"{access.meta['location']} Illegal recursion to name {access.name}")
            access.meta[RESOLVES_TO] = resolves_to
        #end VNameAccess
        case VBlock():
            block: VBlock = node
            with ctx.enter_scope(block.scope):
                if block.label is not None:
                    ctx.current_scope.define(block.label, block)
                for item in block.body:
                    resolve(item, ctx)
        #end VBlock
        case VStringLiteral():
            # TODO - Type inference?
            pass
        #end VStringLiteral
        # Types - should maybe be moved to a dedicated function
        case VNamedType():
            named_type: VNamedType = node
            # Lookup the type in the current scope
            resolves_to = ctx.current_scope.lookup(named_type.name)
            if resolves_to is None:
                raise CompileError(f"{named_type.meta['location']} Undefined type {named_type.name}")
            if ctx.is_illegally_recursive(resolves_to):
                raise CompileError(f"{named_type.meta['location']} Illegal recursion to type {named_type.name}")
            named_type.meta[RESOLVES_TO] = resolves_to
        #end VNamedType
        case _:
            # I think all nodes are going to be here?
            raise TypeError(f"Unexpected node type: {type(node)}")
    #end match
    return None
#end resolve
