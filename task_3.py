"""Завдання 3. Алгоритм Дейкстри з використанням бінарної купи."""

from __future__ import annotations
import heapq
from typing import Dict, Hashable, Iterable, Tuple

Graph = Dict[Hashable, Iterable[Tuple[Hashable, int]]]


def dijkstra(graph: Graph, start: Hashable) -> dict[Hashable, float]:
    """Знаходить найкоротші відстані від стартової вершини до всіх інших."""
    distances: dict[Hashable, float] = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    priority_queue: list[tuple[float, Hashable]] = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def demo() -> None:
    """Демонструє роботу алгоритму на зваженому графі."""
    graph: Graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("F", 6)],
        "E": [("C", 10), ("D", 2), ("F", 3)],
        "F": [("D", 6), ("E", 3)],
    }

    start_vertex = "A"
    distances = dijkstra(graph, start_vertex)

    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")


if __name__ == "__main__":
    demo()
