from typing import Optional, TypeVar
#from vast.declarations import VFunction
from common import NameConflictError
from .base import ScopeItem


# Utility class for descerning various implementations of the same function name
class FuncVariants(ScopeItem):
    __funcs: list = []

    def __init__(self, funcs: list):
        self.__funcs = funcs

    def implement(self, func):
        self.__funcs.append(func)

    # TODO - implement function for finding the best match for signature (function overloading)
    # though - with the current implementation of scopes, this would prioritize
    # the FuncVariant closest to the current scope
    # TODO - find a way to solve the above issue (maybe w/ a separate class for FunctionScope)


I = TypeVar("I",)

# TODO - separate out `FunctionScope` to a child class
class Scope[ItemType]:
    symbols: dict[str, ItemType]
    parent: Optional["Scope"]

    def __init__(self, parent: Optional["Scope"] = None):
        self.symbols = {}
        self.parent = parent

    # def define(self, name: str, value: ItemType):
    #     if name not in self.symbols:
    #         self.symbols[name] = value
    #         return
    #
    #     cur_item = self.symbols[name]
    #
    #     if isinstance(value, VFunction):
    #         if isinstance(cur_item, FuncVariants):
    #             cur_item.implement(value)
    #             return
    #         elif isinstance(cur_item, VFunction):
    #             self.symbols[name] = FuncVariants(funcs=[cur_item, value])
    #             return
    #
    #     raise NameConflictError(f"Name {name} already defined in this scope")

    def lookup(self, name: str) -> Optional[ScopeItem]: # Replace w/ a dunder method?
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.lookup(name)
        return None

# Add a module scope (inheriting from Scope or MultiScope) that could differentiate between public and private symbols?

# class MultiScope:
#     functions: Scope[VFunction]
#     variables: Scope[VVariable]
#     types: Scope[VType]
#     labels: Scope[VBlock]
#
#     def __init__(self, parent: Optional["MultiScope"] = None):
#         self.functions = Scope(parent.functions if parent else None)
#         self.variables = Scope(parent.variables if parent else None)
#         self.types = Scope(parent.types if parent else None)
#         self.labels = Scope(parent.labels if parent else None)

    # Could also add a generic lookup method that would search through all scopes, if context is ambiguous


# class Context:
#     _scope_stack: list[MultiScope] = []
#
#     def __init__(self):
#         self._scope_stack = []
#
#     @property
#     def cur_scope(self):
#         if not self._scope_stack:
#             return None
#         return self._scope_stack[-1]
#
#     def push_scope(self):
#         self._scope_stack.append(
#             MultiScope(parent=self.cur_scope)
#         )
#
#     def pop_scope(self):
#         self._scope_stack.pop()
        