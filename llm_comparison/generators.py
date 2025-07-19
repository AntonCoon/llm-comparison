import collections
from typing import List, Optional

import numpy
import scipy

from llm_comparison.custom_types import Tree


def sample_one_poisson_truncated(lam: float, sharpness: float = 2.0) -> int:
    x_vals = numpy.arange(1, 11)
    probs = scipy.stats.poisson.pmf(x_vals, mu=lam)
    probs = numpy.power(probs, sharpness)
    probs /= probs.sum()
    return int(numpy.random.choice(x_vals, p=probs))


def generate_tree(size: int, density: int, names: List[str]) -> Tree:
    dq = collections.deque()
    root = Tree(val=names[size - 1])
    size -= 1
    dq.append(root)
    while dq and size > 0:
        current_node = dq.popleft()
        limit = sample_one_poisson_truncated(density)
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
    dq = collections.deque()
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


def lca(tree: Tree, q: str, p: str) -> Optional[str]:
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


def depth(tree: Tree) -> int:
    if tree.children[0] is None:
        return 1
    return 1 + max(map(depth, tree.children))
