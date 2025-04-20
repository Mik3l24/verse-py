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
    constness: Constness

    def __init__(self, constness: Constness = Constness.UNSPECIFIED):
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
    name: str # Refers to a type within the scope

    def __init__(self, name, constness: Constness = Constness.UNSPECIFIED, location: Optional[Location] = None):
        super().__init__(constness)
        self.name = name
        self.location = location


@dataclass
class VFundamentalType(VType):
    name: str

    def __init__(self, name, constness: Constness = Constness.UNSPECIFIED, location: Optional[Location] = None):
        super().__init__(constness)
        self.name = name
        self.location = location
    
    def __eq__(self, value: object) -> bool:
        return isinstance(value, VFundamentalType) and self.name == value.name


@dataclass
class VPointerType(VType):
    class Kind(IntEnum):
        POINTER = 0
        REFERENCE = 1

    to: VType
    kind: Kind

    def __init__(self, base_type, kind: Kind, constness: Constness = Constness.UNSPECIFIED, location: Optional[Location] = None):
        super().__init__(constness)
        self.to = base_type
        self.kind = kind
        self.location = location

    def __eq__(self, value: object) -> bool:
        return isinstance(value, VPointerType) and self.to == value.to

