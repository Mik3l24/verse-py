from enum import Enum
from .expressions import VExpression, VAccess


class VStatement:
    pass


class VAssignment(VStatement):
    target: VAccess
    value: VExpression

    def __init__(self, target: VExpression, value: VExpression):
        self.target = target
        self.value = value


# Variable declaration isn't at the moment a statement...
# But the optional assignment within it is and its placement is important to get the order of instructions right.
# Make it a statement within declarations.py?
# ... or introduce a proxy statement here?
# ... or automatically insert the assignment statement in the transformer?
#     The transformer could then just not do the assignment statement if the variable is inline, 
#     as the expression should be copied as is anyway.


class VCall(VStatement):
    func: VAccess
    targets: list[VAccess]
    args: list[VExpression]

    def __init__(self, func: VAccess, targets: list[VAccess] = [], args: list[VExpression] = []):
        self.func = func
        self.args = args


class VReturn(VStatement):
    values: list[VExpression]

    def __init__(self, values: list[VExpression]):
        self.values = values


class VBreak(VStatement):
    class Variant(Enum):
        BREAK = 0
        CONTINUE = 1
    variant: Variant
    label: str

    def __init__(self, variant: Variant, label: str = ""):
        self.variant = variant
        self.label = label


class VBlock(VStatement):
    body: list[VStatement]
    label: str

    def __init__(self, body: list[VStatement] = [], label: str = ""):
        self.body = body
        self.label = label


class VIf(VBlock):
    cond: VExpression
    else_block: VBlock

    def __init__(self, cond: VExpression, body: list[VStatement] = [], else_block: VBlock = VBlock(), label: str = ""):
        super().__init__(body, label=label)
        self.cond = cond
        self.else_block = else_block


class VWhile(VBlock):
    cond: VExpression

    def __init__(self, cond: VExpression, body: list[VStatement] = [], label: str = ""):
        super().__init__(body, label=label)
        self.cond = cond

