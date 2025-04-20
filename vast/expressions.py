from dataclasses import dataclass
from enum import StrEnum
from typing import Optional

from .base import VASTNode, Location
from .types import VType, VFundamentalType


@dataclass
class VExpression(VASTNode):
    type: Optional[VType]

    def __init__(self):
        super().__init__(None)
        self.type = None

    def type_eval(self):
        raise NotImplementedError(f"Type evaluation not implemented for {self.__class__.__name__}")


@dataclass
class VLiteral(VExpression):
    value: any

    def __init__(self, value: any, type: VType, location: Optional[Location] = None):
        super().__init__()
        self.value = value
        self.type = type
        self.location = location
    

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
    
    l: VExpression
    r: VExpression
    op: Op

    def __init__(self, l: VExpression, r: VExpression, op: Op, location: Optional[Location] = None):
        super().__init__()
        self.l = l
        self.r = r
        self.op = op
        self.location = location



@dataclass
class VUnaryOp(VExpression):
    class Op(StrEnum):
        NEG = "-"
        NOT = "!"
        BITNOT = "~"
    
    expr: VExpression
    op: Op

    def __init__(self, expr: VExpression, op: Op, location: Optional[Location] = None):
        super().__init__()
        self.expr = expr
        self.op = op
        self.location = location



@dataclass
class VCast(VExpression):
    expr: VExpression
    to: VType

    def __init__(self, expr: VExpression, to: VType, location: Optional[Location] = None):
        super().__init__()
        self.expr = expr
        self.to = to
        self.location = location


class VAccess(VExpression):
    pass


@dataclass
class VNameAccess(VAccess):
    name: str

    def __init__(self, name: str, location: Optional[Location] = None):
        super().__init__()
        self.name = name
        self.location = location


@dataclass
class VMemberAccess(VAccess):
    expr: VExpression
    member: str

    def __init__(self, expr: VExpression, member: str, location: Optional[Location] = None):
        super().__init__()
        self.expr = expr
        self.member = member
        self.location = location


@dataclass
class VArrayAccess(VAccess):
    arr: VExpression
    index: VExpression

    def __init__(self, arr: VExpression, index: VExpression, location: Optional[Location] = None):
        super().__init__()
        self.arr = arr
        self.index = index
        self.location = location


@dataclass
class VDeref(VAccess):
    expr: VExpression


@dataclass
class VExprCall(VExpression):
    func: VExpression
    targets: list[VAccess]
    args: list[VExpression]
