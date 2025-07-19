from typing import Dict, List, Tuple

import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt

from llm_comparison.custom_types import Tree


def layout_tree(
    tree: Tree, x=0, y=0, x_spacing=1, y_spacing=1
) -> Tuple[Dict[Tree, Tuple[float, float]]]:
    if tree is None:
        return {}, 0
    child_positions = []
    width = 0
    positions = {}
    for child in tree.children:
        child_pos, child_width = layout_tree(
            child, x + width, y - y_spacing, x_spacing, y_spacing
        )
        positions.update(child_pos)
        child_positions.append((child, width + child_width / 2))
        width += child_width + x_spacing
    if child_positions:
        child_xs = [x + cx for _, cx in child_positions]
        center_x = sum(child_xs) / len(child_xs)
    else:
        center_x = x
        width = 1
    positions[tree] = (center_x, y)
    return positions, width


def draw_tree(ax: matplotlib.axes.Axes, tree: True) -> None:
    positions, _ = layout_tree(tree)
    for node, (x, y) in positions.items():
        circle = patches.Circle((x, y), 0.3, color="lightblue", ec="black")
        ax.add_patch(circle)
        for child in node.children:
            if child in positions:
                cx, cy = positions[child]
                ax.plot([x, cx], [y - 0.3, cy + 0.3], "k-", linewidth=1)
    all_x, all_y = zip(*positions.values())
    ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
    ax.set_ylim(min(all_y) - 1, max(all_y) + 1)
    ax.set_aspect("equal")
    ax.axis("off")


def visualize_tree_grid(
    trees_2d: List[List[Tree]],
    parameters: List[List[int]],
    figsize: Tuple[int, int] = (12, 8),
) -> None:
    rows, cols = len(trees_2d), len(trees_2d[0])
    _, axes = plt.subplots(rows, cols, figsize=figsize)
    if rows == 1 and cols == 1:
        axes = [[axes]]
    elif rows == 1:
        axes = [axes]
    elif cols == 1:
        axes = [[ax] for ax in axes]
    for i in range(rows):
        for j in range(cols):
            draw_tree(axes[i][j], trees_2d[i][j])
            axes[i][j].set_title(f"Tree {parameters[i][j]}", fontsize=10)
    plt.tight_layout()
    plt.show()
