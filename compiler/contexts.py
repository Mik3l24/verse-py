from enum import Enum
from typing import Optional

from vast.scope import Scope


class CompileContext:
    class Recursion(Enum):
        ALLOWED = 0
        DISALLOWED = 1
    scopes: list[Scope]
    current_scope: Optional[Scope]

    parenthood_stack: list[tuple[object, Recursion]]


    def __init__(self, initial_scope: Optional[Scope] = None):
        self.scopes = [initial_scope] or []
        self.current_scope = initial_scope
        self.parenthood_stack = []

    ## Scope management methods ##
    def push_scope(self, scope: Scope):
        if scope is None:
            raise ValueError("Cannot push a None scope.")
        if scope in self.scopes:
            raise ValueError("Cannot push the same scope twice.")

        # Establish the parent-child relationship (should it be done here?)
        if self.current_scope is not None and scope.parent is None:
            scope.parent = self.current_scope
        self.scopes.append(scope)
        self.current_scope = scope


    def pop_scope(self):
        if self.scopes:
            self.scopes.pop()
            self.current_scope = self.scopes[-1] if self.scopes else None

    def enter_scope(self, scope: Scope):
        ctx = self
        class ScopeContext:
            def __enter__(self):
                ctx.push_scope(scope)
                return ctx.current_scope

            def __exit__(self, exc_type, exc_val, exc_tb):
                ctx.pop_scope()
        # I freaking love python TODO - remove this silly comment
        return ScopeContext()

    ## Recursion management methods ##
    def enter_parenthood(self, node, allow_recursion: Recursion = Recursion.DISALLOWED):
        ctx = self
        class RecursionContext:
            def __enter__(self):
                ctx.parenthood_stack.append((node, allow_recursion))
                return ctx

            def __exit__(self, exc_type, exc_val, exc_tb):
                ctx.parenthood_stack.pop()
        return RecursionContext()

    def is_legally_recursive(self, node):
        return any(node is n for n, r in self.parenthood_stack if r == self.Recursion.ALLOWED)

    def is_illegally_recursive(self, node):
        return any(node is n for n, r in self.parenthood_stack if r == self.Recursion.DISALLOWED)

    def last_recursion_parent(self):
        return self.parenthood_stack[-1] if self.parenthood_stack else None