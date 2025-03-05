from enum import StrEnum
from typing import Optional
from .types import VType, FundamentalType


class VExpression:
    type: Optional[VType]

    def type_eval(self):
        raise NotImplementedError(f"Type evaluation not implemented for {self.__class__.__name__}")


class VLiteral(VExpression):
    value: any

    def __init__(self, value: any, vtype: FundamentalType):
        self.value = value
        self.type = vtype
    

class VBinaryOp(VExpression):
    class Op(StrEnum):
        ADD = "+"
        SUB = "-"
        MULT = "*"
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

    def __init__(self, l: VExpression, r: VExpression, op: Op):
        self.l = l
        self.r = r
        self.op = op


class VUnaryOp(VExpression):
    class Op(StrEnum):
        NEG = "-"
        NOT = "!"
        BITNOT = "~"
    
    expr: VExpression
    op: Op

    def __init__(self, expr: VExpression, op: Op):
        self.expr = expr
        self.op = op


class VCast(VExpression):
    expr: VExpression
    to: VType

    def __init__(self, expr: VExpression, to: VType):
        self.expr = expr
        self.to = to


class VAccess(VExpression):
    pass


class VVariableAccess(VAccess):
    name: str

    def __init__(self, name: str):
        self.name = name


class VMemberAccess(VAccess):
    expr: VExpression
    member: str

    def __init__(self, expr: VExpression, member: str):
        self.expr = expr
        self.member = member


class VArrayAccess(VAccess):
    arr: VExpression
    index: VExpression

    def __init__(self, arr: VExpression, index: VExpression):
        self.arr = arr
        self.index = index


class VDeref(VAccess):
    expr: VExpression

    def __init__(self, expr: VExpression):
        self.expr = expr


class VCall(VExpression):
    func: VExpression
    args: list[VExpression]

    def __init__(self, func: VExpression, args: list[VExpression]):
        self.func = func
        self.args = args
