from contexts import CompileContext

from common.errors import ObjectAlreadyDefinedException
from vast import *
from vast.scope import Scope


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
                case _:
                    # We may have other unnamed types of items in the module in the future, that we may want to ignore
                    # For now, we will just raise an error if we encounter an unexpected item type.
                    raise TypeError(f"Unexpected item type: {type(item)}")
        # Step 2
        for item in root.items:
            resolve(item, ctx)

    #end with
#end module_register


def register_if_not_registered(node: ScopeItem, ctx: CompileContext):
    """
    Only use for nodes that can be directly in the module!
    :param node:
    :param ctx:
    :return:
    """
    try:
        ctx.current_scope.define(node.name, node)
    except ObjectAlreadyDefinedException:
        pass

def resolve(node, ctx: CompileContext):
    """
    First major pass of the compiler.
    This pass will register names in the module's scope and resolve the names to the ScopeItems they refer to.
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

            register_if_not_registered(decl, ctx)
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

        #end VFunction
        case VVariable():
            var: VVariable = node
            register_if_not_registered(var, ctx)

            if var.init_value is not None:
                with ctx.enter_parenthood(var):
                    resolve(var.init_value, ctx)

            # TODO - implement type inference here, once it's also in grammar?
            resolve(var.type, ctx)
        #end VVariable




        case _:
            # I think all nodes are going to
            raise TypeError(f"Unexpected node type: {type(node)}")
    #end match
#end resolve
