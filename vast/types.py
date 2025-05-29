from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

from .base import ScopeItem, VASTNode, Location


class Constness(IntEnum):
    UNSPECIFIED = 0
    VARIABLE = 1
    CONSTANT = 2


@dataclass
class VType(VASTNode, ScopeItem):
    constness: Constness = Constness.UNSPECIFIED

    def __init__(self, meta: dict, constness: Constness = Constness.UNSPECIFIED):
        super().__init__(meta)
        self.constness = constness
    
    def __eq__(self, value: object) -> bool:
        raise NotImplementedError("Equality not implemented for the base class VType")


# Virtual types cannot be type-checked, 
# they are placeholders for real types until they get resolved.
class VVirtualType(VType):
    def __eq__(self, value: object) -> bool:
        raise NotImplementedError("Cannot type-check virtual types")


@dataclass
class VNamedType(VVirtualType):
    name: str = "" # Refers to a type within the scope

    def __init__(self, name, constness: Constness = Constness.UNSPECIFIED, meta: dict = None):
        super().__init__(meta, constness)
        self.name = name


@dataclass
class VFundamentalType(VType):
    class T(IntEnum):
        ANY = 0
        INT = 1
        UINT = 2
        FLOAT = 3
    class Bits(IntEnum):
        UNSPECIFIED = 0
        b8 = 8
        b16 = 16
        b32 = 32
        b64 = 64
    t: T = T.ANY
    bits: Bits = Bits.UNSPECIFIED

    def __init__(self, t: T, bits: Bits, constness: Constness = Constness.UNSPECIFIED, meta: dict = None):
        super().__init__(meta, constness)
        self.t = t
        self.bits = bits
    
    def __eq__(self, value: object) -> bool:
        return isinstance(value, VFundamentalType) and self.t == value.t and self.bits == value.bits


@dataclass
class VPointerType(VType):
    class Kind(IntEnum):
        POINTER = 0
        REFERENCE = 1

    to: VType = None
    kind: Kind = Kind.POINTER

    def __init__(self, base_type, kind: Kind, constness: Constness = Constness.UNSPECIFIED, meta: dict = None):
        super().__init__(meta, constness)
        self.to = base_type
        self.kind = kind

    def __eq__(self, value: object) -> bool:
        return isinstance(value, VPointerType) and self.to == value.to

