"""Завдання 1. Однозв'язний список: реверс, сортування та злиття."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class Node:
    """Вузол однозв'язного списку."""

    data: int
    next: Optional["Node"] = None


class LinkedList:
    """Простий однозв'язний список для демонстрації алгоритмів."""

    def __init__(self, values: Iterable[int] | None = None):
        self.head: Optional[Node] = None
        if values is not None:
            for value in values:
                self.append(value)

    def append(self, data: int) -> None:
        """Додає новий елемент у кінець списку."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_list(self) -> list[int]:
        """Повертає значення списку у вигляді Python-списку."""
        result: list[int] = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self) -> str:
        return " -> ".join(map(str, self.to_list())) if self.head else "Empty list"


def reverse_linked_list(head: Optional[Node]) -> Optional[Node]:
    """Реверсує список, змінюючи посилання між вузлами."""
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def get_middle(head: Node) -> Node:
    """Знаходить середину списку для сортування злиттям."""
    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next  # type: ignore[assignment]
        fast = fast.next.next

    return slow


def merge_sorted_lists(first: Optional[Node], second: Optional[Node]) -> Optional[Node]:
    """Об'єднує два відсортовані списки в один відсортований список."""
    dummy = Node(0)
    tail = dummy

    while first is not None and second is not None:
        if first.data <= second.data:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next
        tail = tail.next

    tail.next = first if first is not None else second
    return dummy.next


def merge_sort(head: Optional[Node]) -> Optional[Node]:
    """Сортує однозв'язний список алгоритмом сортування злиттям."""
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    second_half = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(second_half)

    return merge_sorted_lists(left, right)


def demo() -> None:
    """Демонструє роботу всіх функцій завдання."""
    linked_list = LinkedList([4, 2, 7, 1, 3])
    print("Початковий список:", linked_list)

    linked_list.head = reverse_linked_list(linked_list.head)
    print("Після реверсування:", linked_list)

    linked_list.head = merge_sort(linked_list.head)
    print("Після сортування:", linked_list)

    first = LinkedList([1, 3, 5, 7])
    second = LinkedList([2, 4, 6, 8])
    merged = LinkedList()
    merged.head = merge_sorted_lists(first.head, second.head)
    print("Об'єднаний відсортований список:", merged)


if __name__ == "__main__":
    demo()
