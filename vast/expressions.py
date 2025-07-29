from dataclasses import dataclass
from enum import StrEnum
from typing import Optional

from .base import VASTNode, Location
from .types import VType, VFundamentalType


@dataclass
class VExpression(VASTNode):
    type: Optional[VType]

    def __init__(self, meta: dict = None):
        super().__init__(meta)
        self.type = None

    def type_eval(self):
        raise NotImplementedError(f"Type evaluation not implemented for {self.__class__.__name__}")


@dataclass
class VLiteral(VExpression):
    def __init__(self, meta: dict = None):
        super().__init__(meta)


@dataclass
class VIntLiteral(VLiteral):
    value: int
    def __init__(self, value: any, type: VType, meta: dict = None):
        super().__init__(meta)
        self.value = value
        self.type = type


class VStringLiteral(VLiteral):
    value: str
    def __init__(self, value: any, type: VType, meta: dict = None):
        super().__init__()
        self.value = value
        self.type = type
        self.meta = meta


@dataclass
class VBinaryOp(VExpression):
    class Op(StrEnum):
        ADD = "+"
        SUB = "-"
        TIMES = "*"
        DIV = "/"
        MOD = "%"
        AND = "&&"
        OR = "||"
        BITAND = "&"
        BITOR = "|"
        BITXOR = "^"
        EQUAL = "=="
        NOTEQ = "!="
        LESS = "<"
        GREATER = ">"
        LESSEQ = "<="
        GREATEREQ = ">="
    
    l: VExpression = None
    r: VExpression = None
    op: Op = Op.ADD

    def __init__(self, l: VExpression, r: VExpression, op: Op, meta: dict = None):
        super().__init__(meta)
        self.l = l
        self.r = r
        self.op = op



@dataclass
class VUnaryOp(VExpression):
    class Op(StrEnum):
        NEG = "-"
        NOT = "!"
        BITNOT = "~"
    
    expr: VExpression = None
    op: Op = Op.NOT

    def __init__(self, expr: VExpression, op: Op, meta: dict = None):
        super().__init__(meta)
        self.expr = expr
        self.op = op



@dataclass
class VCast(VExpression):
    expr: VExpression
    to: VType

    def __init__(self, expr: VExpression, to: VType, meta: dict = None):
        super().__init__(meta)
        self.expr = expr
        self.to = to


class VAccess(VExpression):
    pass


@dataclass
class VNameAccess(VAccess):
    name: str

    def __init__(self, name: str, meta: dict = None):
        super().__init__(meta)
        self.name = name


@dataclass
class VMemberAccess(VAccess):
    expr: VExpression
    member: str

    def __init__(self, expr: VExpression, member: str, meta: dict = None):
        super().__init__(meta)
        self.expr = expr
        self.member = member


@dataclass
class VArrayAccess(VAccess):
    arr: VExpression
    index: VExpression

    def __init__(self, arr: VExpression, index: VExpression, meta: dict = None):
        super().__init__(meta)
        self.arr = arr
        self.index = index


@dataclass
class VDeref(VAccess):
    expr: VExpression


@dataclass
class VExprCall(VExpression):
    func: VExpression
    targets: list[VAccess]
    args: list[VExpression]
