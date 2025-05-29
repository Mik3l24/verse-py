from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

from vast.scope import Scope
from .base import VASTNode, Location
from .expressions import VExpression, VAccess


class VStatement(VASTNode):
    pass


class VAssignment(VStatement):
    target: VAccess
    value: VExpression

    def __init__(self, target: VAccess, value: VExpression, meta: dict = None):
        super().__init__(meta)
        self.target = target
        self.value = value



# Variable declaration isn't at the moment a statement...
# But the optional assignment within it is and its placement is important to get the order of instructions right.
# Make it a statement within declarations.py?
# ... or introduce a proxy statement here?
# ... or automatically insert the assignment statement in the transformer?
#     The transformer could then just not do the assignment statement if the variable is inline, 
#     as the expression should be copied as is anyway.


@dataclass
class VCall(VStatement, VExpression):
    func: VAccess
    targets: list[VAccess]
    args: list[VExpression]

    def __init__(self, func: VAccess, targets: list[VAccess], args: list[VExpression], meta: dict = None):
        super().__init__(meta)
        self.func = func
        self.targets = targets
        self.args = args


@dataclass
class VReturn(VStatement):
    values: list[VExpression] = None

    def __init__(self, values: list[VExpression], meta: dict = None):
        super().__init__(meta)
        self.values = values


@dataclass
class VBreak(VStatement):
    class Kind(Enum):
        BREAK = 0
        CONTINUE = 1
    kind: Kind
    label: str

    def __init__(self, kind: Kind, label: str = "", meta: dict = None):
        super().__init__(meta)
        self.kind = kind
        self.label = label


@dataclass
class VBlock(VStatement):
    body: list[VStatement] 
    label: Optional[str]
    scope: Scope

    def __init__(self, body: list[VStatement], label: Optional[str] = None, scope: Optional[Scope] = None,
                 meta: dict = None):
        super().__init__(meta)
        self.body = body
        self.label = label
        self.scope = scope if scope is not None else Scope()


@dataclass
class VIf(VStatement):
    cond: VExpression
    block: VBlock
    else_block: Optional[Union["VIf", VBlock]] = None

    def __init__(self, cond: VExpression, block: VBlock, else_block: VBlock = None, meta: dict = None):
        super().__init__(meta)
        self.cond = cond
        self.block = block
        self.else_block = else_block


@dataclass
class VWhile(VStatement):
    cond: VExpression
    block: VBlock
    is_do_while: bool

    def __init__(self, cond: VExpression, block: VBlock, is_do_while: bool, meta: dict = None):
        super().__init__(meta)
        self.cond = cond
        self.block = block
        self.is_do_while = is_do_while

