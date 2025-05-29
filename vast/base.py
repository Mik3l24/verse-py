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
    meta: dict

    def __init__(self, meta: dict = None) -> None:
        self.meta = meta or dict()
