from typing import List, Union, Optional
import random
from collections import deque


class Tree():
    def __init__(self, val: Union[str, int], children: Optional[List["Tree"]] = [None]):
        self.value: str = val
        self.children: Optional[List["Tree"]] = children[:]


def generate_tree(size: int, density: int, names: List[str]) -> Tree:
    dq = deque()
    root = Tree(val=names[size - 1])
    size -= 1
    dq.append(root)
    while dq and size > 0:
        current_node = dq.popleft()
        limit = int(1 + density * random.random())
        children = []
        for _ in range(limit):
            children.append(Tree(val=names[size - 1]))
            dq.append(children[-1])
            size -= 1
            if size <= 0:
                break
        if children:
            current_node.children = children[:]
    return root


def tree_to_text(tree: Tree) -> str:
    result = []
    dq = deque()
    dq.append(tree)
    while dq:
        node = dq.popleft()
        result.append(f"{node.value} is parent for ")
        children_names = []
        for child in node.children:
            if child:
                children_names.append(child.value)
                dq.append(child)
        if children_names:
            result[-1] += " and ".join(children_names)
        else:
            result[-1] += "no one"
    return ". ".join(result)


def lca(tree: Tree, q: str, p: str) -> str:
    if tree.value == q or tree.value == p:
        return tree.value
    result = []
    for child in tree.children:
        if child:
            result.append(lca(child, p, q))
        else:
            result.append(None)
    result = [item for item in result if item]
    if len(result) > 1:
        return tree.value
    if len(result) == 1:
        return result[0]
    return None
