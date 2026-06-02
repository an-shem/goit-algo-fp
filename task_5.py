"""Завдання 5. Візуалізація обходу бінарного дерева DFS та BFS."""

from __future__ import annotations
from collections import deque
from typing import Callable
from task_4 import Node, draw_tree, heap_to_tree


def generate_color(step: int, total: int) -> str:
    """Генерує унікальний колір від темного до світлого відтінку."""
    if total <= 1:
        value = 255
    else:
        value = 40 + int(215 * step / (total - 1))

    # Від темно-синього до світло-блакитного відтінку.
    red = int(value * 0.25)
    green = int(value * 0.6)
    blue = value
    return f"#{red:02X}{green:02X}{blue:02X}"


def count_nodes(root: Node | None) -> int:
    """Підраховує кількість вузлів за допомогою черги, без рекурсії."""
    if root is None:
        return 0

    count = 0
    queue: deque[Node] = deque([root])

    while queue:
        node = queue.popleft()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return count


def reset_colors(root: Node | None, color: str = "skyblue") -> None:
    """Повертає початковий колір усім вузлам без рекурсії."""
    if root is None:
        return

    queue: deque[Node] = deque([root])
    while queue:
        node = queue.popleft()
        node.color = color
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs_traversal(root: Node | None) -> list[Node]:
    """Виконує DFS за допомогою стеку, без рекурсії."""
    if root is None:
        return []

    result: list[Node] = []
    stack: list[Node] = [root]

    while stack:
        node = stack.pop()
        result.append(node)

        # Спочатку додаємо правого нащадка, щоб лівий обробився першим.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def bfs_traversal(root: Node | None) -> list[Node]:
    """Виконує BFS за допомогою черги, без рекурсії."""
    if root is None:
        return []

    result: list[Node] = []
    queue: deque[Node] = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def colorize_traversal(root: Node | None, traversal_function: Callable[[Node | None], list[Node]]) -> list[int]:
    """Розфарбовує вузли відповідно до порядку обходу."""
    traversal = traversal_function(root)
    total = len(traversal)

    for step, node in enumerate(traversal):
        node.color = generate_color(step, total)

    return [node.val for node in traversal]


def visualize_traversals(root: Node) -> None:
    """Візуалізує DFS та BFS для одного дерева."""
    reset_colors(root)
    dfs_order = colorize_traversal(root, dfs_traversal)
    print("Порядок DFS:", dfs_order)
    draw_tree(root, "Обхід у глибину (DFS)")

    reset_colors(root)
    bfs_order = colorize_traversal(root, bfs_traversal)
    print("Порядок BFS:", bfs_order)
    draw_tree(root, "Обхід у ширину (BFS)")


def demo() -> None:
    """Створює дерево з купи та демонструє обходи."""
    heap = [1, 3, 5, 7, 9, 8, 10, 12, 15]
    root = heap_to_tree(heap)
    if root is None:
        print("Дерево порожнє")
        return

    visualize_traversals(root)


if __name__ == "__main__":
    demo()
