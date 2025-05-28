from dataclasses import dataclass
from typing import Optional

from vast.scope import Scope
from .declarations import VModuleItem
from .base import VASTNode, ScopeItem, Location


@dataclass
class VModuleBase(VASTNode):
    items: list[VModuleItem]

@dataclass
class VSection(VModuleBase, VModuleItem):
    # TODO - Implement
    pass


@dataclass
class VModule(VModuleBase, ScopeItem):

    name: Optional[str]
    scope: Scope

    def __init__(self, items: list[VModuleItem], name: Optional[str] = None, scope: Optional[Scope] = None, location: Optional[Location] = None):
        self.items = items
        self.name = name
        self.scope = scope if scope is not None else Scope()
        self.location = location


