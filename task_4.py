"""Завдання 4. Візуалізація бінарної купи."""

from __future__ import annotations
import uuid
from typing import Optional
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    """Вузол бінарного дерева."""

    def __init__(self, key: int, color: str = "skyblue"):
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: dict, x: float = 0, y: float = 0, layer: int = 1) -> nx.DiGraph:
    """Додає вузли та ребра дерева до графа NetworkX."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2**layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2**layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root: Node, title: str = "Бінарне дерево") -> None:
    """Візуалізує дерево за допомогою NetworkX та Matplotlib."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap: list[int]) -> Optional[Node]:
    """Створює бінарне дерево з масиву, який представляє бінарну купу."""
    if not heap:
        return None

    nodes = [Node(value) for value in heap]

    for index in range(len(nodes)):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(nodes):
            nodes[index].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[index].right = nodes[right_index]

    return nodes[0]


def visualize_heap(heap: list[int]) -> None:
    """Візуалізує бінарну купу як дерево."""
    root = heap_to_tree(heap)
    if root is None:
        print("Купа порожня")
        return

    draw_tree(root, "Візуалізація бінарної купи")


def demo() -> None:
    """Демонструє візуалізацію мінімальної бінарної купи."""
    heap = [1, 3, 5, 7, 9, 8, 10, 12, 15]
    visualize_heap(heap)


if __name__ == "__main__":
    demo()
