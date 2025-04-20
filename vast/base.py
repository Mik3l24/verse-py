from dataclasses import dataclass
from typing import Optional


class ScopeItem:
    pass

@dataclass
class Location:
    line: int
    column: int


@dataclass
class VASTNode:
    location: Optional[Location]
