from enum import Enum
from typing import Optional
from .types import VType
from .expressions import VExpression
from common import ScopeItem



class VDeclaration(ScopeItem):
    pass


class VVariable(VDeclaration):
    name: str
    type: VType
    init_value: Optional[VExpression]
    inline: bool

    def __repr__(self):
        return f"VVariable({self.name}, {self.type}, {self.init_value})"


class VFunction(VDeclaration):
    name: str # Should there be a name here, since it's going to be in the scope's dict?
    args: list[VVariable]
    body: list
    return_types: list[VType]
    inline: bool

    def __repr__(self):
        return f"VFunction({self.name}, {self.args}, {self.body})"




