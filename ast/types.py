from enum import IntEnum
from common import ScopeItem


class Mut(IntEnum):
    UNSPECIFIED = 0
    VARIABLE = 1
    CONSTANT = 2


class VType(ScopeItem):
    mutability: Mut

    def __init__(self, mutability: Mut = Mut.UNSPECIFIED):
        self.mutability = mutability
    
    def __eq__(self, value: object) -> bool:
        raise NotImplementedError("Equality not implemented for the base class VType")


# Virtual types cannot be type-checked, 
# they are placeholders for real types until they get resolved.
class VVirtualType(VType):
    def __eq__(self, value: object) -> bool:
        raise NotImplementedError("Cannot type-check virtual types")


class VNamedType(VVirtualType):
    name: str # Refers to a type within the scope

    def __init__(self, name, mutability: Mut = Mut.UNSPECIFIED):
        super().__init__(mutability)
        self.name = name


class VFundamentalType(VType):
    name: str

    def __init__(self, name, mutability: Mut = Mut.UNSPECIFIED):
        super().__init__(mutability)
        self.name = name
    
    def __eq__(self, value: object) -> bool:
        return isinstance(value, VFundamentalType) and self.name == value.name


class VPointerType(VType):
    to: VType

    def __init__(self, base_type, mutability: Mut = Mut.UNSPECIFIED):
        super().__init__(mutability)
        self.to = base_type

    def __eq__(self, value: object) -> bool:
        return isinstance(value, VPointerType) and self.to == value.to

