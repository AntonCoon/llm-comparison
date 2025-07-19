from dataclasses import dataclass
from typing import List, Optional, Union


class Tree:
    def __init__(self, val: Union[str, int], children: Optional[List["Tree"]] = [None]):
        self.value: str = val
        self.children: Optional[List["Tree"]] = children[:]


@dataclass
class QAExample:
    tree: Tree
    text: str
    query: str
    answer: str
