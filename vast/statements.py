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

    def __init__(self, target: VAccess, value: VExpression, location: Optional[Location] = None):
        self.target = target
        self.value = value
        self.location = location



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

    def __init__(self, func: VAccess, targets: list[VAccess], args: list[VExpression], location: Optional[Location] = None):
        super().__init__()
        self.func = func
        self.targets = targets
        self.args = args
        self.location = location


@dataclass
class VReturn(VStatement):
    values: list[VExpression]

    def __init__(self, values: list[VExpression], location: Optional[Location] = None):
        self.values = values
        self.location = location


@dataclass
class VBreak(VStatement):
    class Kind(Enum):
        BREAK = 0
        CONTINUE = 1
    kind: Kind
    label: str

    def __init__(self, kind: Kind, label: str = "", location: Optional[Location] = None):
        self.kind = kind
        self.label = label
        self.location = location


@dataclass
class VBlock(VStatement):
    body: list[VStatement]
    label: Optional[str]
    scope: Scope

    def __init__(self, body: list[VStatement], label: Optional[str] = None, scope: Optional[Scope] = None, location: Optional[Location] = None):
        self.body = body
        self.label = label
        self.scope = scope if scope is not None else Scope()
        self.location = location


@dataclass
class VIf(VStatement):
    cond: VExpression
    block: VBlock
    else_block: Optional[Union["VIf", VBlock]] = None


@dataclass
class VWhile(VStatement):
    cond: VExpression
    block: VBlock
    is_do_while: bool

