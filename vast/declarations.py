from dataclasses import dataclass
from enum import Enum, IntFlag

from typing import Optional

from .statements import VBlock
from .types import VType
from .expressions import VExpression
from .base import VASTNode, ScopeItem


class Qualifiers(IntFlag):
    # Common
    NONE       = 0b_0000_0000
    INLINE     = 0b_0000_0001
    EXTERNAL   = 0b_0000_1000
    # Function-only
    ENTRYPOINT = 0b_0001_0000



# Base classes
@dataclass
class VModuleItem(VASTNode):
    pass

@dataclass
class VDeclaration(VModuleItem, ScopeItem):
    pass


@dataclass
class VTypeDeclaration(VDeclaration):
    name: str
    type: VType

    def __init__(self, name: str, type: VType, meta: dict = None):
        super().__init__(meta)
        self.name = name
        self.type = type


@dataclass
class VVariable(VDeclaration):
    name: str
    type: VType
    init_value: Optional[VExpression]
    qualifiers: Qualifiers

    def __init__(self, name: str, type: VType, init_value: Optional[VExpression] = None, qualifiers: Qualifiers = Qualifiers.NONE, meta: dict = None):
        super().__init__(meta)
        self.name = name
        self.type = type
        self.init_value = init_value
        self.qualifiers = qualifiers


class VArgument(VVariable):
    pass


@dataclass
class VFunction(VDeclaration):
    class ExternKind(Enum):
        NOT_EXTERN = "__NotExtern__"
        VERBOSE = "Verbose"
        C = "C"
    name: str
    extern_kind: ExternKind
    extern_name: Optional[str]
    targets: list[VArgument]
    args: list[VArgument]
    return_type: VType
    qualifiers: Qualifiers
    body: VBlock

    # TODO - Add a VFunctionSignature getter and class

    def __init__(self, name: str, extern_kind: ExternKind = ExternKind.NOT_EXTERN, extern_name: Optional[str] = None,
                 targets: list[VArgument] = None, args: list[VArgument] = None, return_type: VType = None,
                 qualifiers: Qualifiers = Qualifiers.NONE, body: VBlock = None, meta: dict = None):
            super().__init__(meta)
            self.name = name
            self.extern_kind = extern_kind
            self.extern_name = extern_name
            self.targets = targets if targets is not None else []
            self.args = args if args is not None else []
            self.return_type = return_type
            self.qualifiers = qualifiers
            self.body = body if body is not None else VBlock(body=[])


