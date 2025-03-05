from typing import Optional
from .declarations import VFunction
from common import NameConflictError, ScopeItem


# Utility class for descerning various implementations of the same function name
class FuncVariants(ScopeItem):
    __funcs: list[VFunction] = []

    def __init__(self, funcs: list[VFunction]):
        self.__funcs = funcs

    def implement(self, func: VFunction):
        self.__funcs.append(func)


class Scope:
    symbols: dict[str, ScopeItem]
    parent: Optional["Scope"]

    def __init__(self, parent: Optional["Scope"] = None):
        self.symbols = {}
        self.parent = parent
    
    def define(self, name: str, value: ScopeItem):
        if name not in self.symbols:
            self.symbols[name] = value
            return
        
        cur_item = self.symbols[name]

        if isinstance(value, VFunction):
            if isinstance(cur_item, FuncVariants):
                cur_item.implement(value)
                return
            elif isinstance(cur_item, VFunction):
                self.symbols[name] = FuncVariants(funcs=[cur_item, value])
                return
        
        raise NameConflictError(f"Name {name} already defined in this scope")

    def lookup(self, name: str) -> Optional[ScopeItem]:
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.lookup(name)
        return None

# Add a module scope (inheriting from Scope) that could differentiate between public and private symbols?


class Context:
    _scope_stack: list[Scope]

    def __init__(self):
        self._scope_stack = []

    @property
    def cur_scope(self):
        if not self._scope_stack:
            return None
        return self._scope_stack[-1]
    
    def push_scope(self):
        self._scope_stack.append(
            Scope(parent=self.cur_scope)
        )
    
    def pop_scope(self):
        self._scope_stack.pop()
        