"""Завдання 6. Жадібний алгоритм та динамічне програмування."""

from __future__ import annotations
from typing import Dict, Tuple

Items = Dict[str, Dict[str, int]]

items: Items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items_data: Items, budget: int) -> tuple[list[str], int, int]:
    """Обирає страви за найбільшим співвідношенням калорій до вартості."""
    sorted_items = sorted(
        items_data.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    selected_items: list[str] = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items_data: Items, budget: int) -> tuple[list[str], int, int]:
    """Знаходить оптимальний набір страв за допомогою динамічного програмування."""
    names = list(items_data.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name = names[i - 1]
        cost = items_data[item_name]["cost"]
        calories = items_data[item_name]["calories"]

        for current_budget in range(budget + 1):
            if cost <= current_budget:
                dp[i][current_budget] = max(
                    dp[i - 1][current_budget],
                    dp[i - 1][current_budget - cost] + calories,
                )
            else:
                dp[i][current_budget] = dp[i - 1][current_budget]

    selected_items: list[str] = []
    current_budget = budget

    for i in range(n, 0, -1):
        if dp[i][current_budget] != dp[i - 1][current_budget]:
            item_name = names[i - 1]
            selected_items.append(item_name)
            current_budget -= items_data[item_name]["cost"]

    selected_items.reverse()
    total_cost = sum(items_data[item]["cost"] for item in selected_items)
    total_calories = sum(items_data[item]["calories"] for item in selected_items)

    return selected_items, total_cost, total_calories


def demo() -> None:
    """Порівнює два підходи для заданого бюджету."""
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(f"Бюджет: {budget}")
    print("Жадібний алгоритм:")
    print(f"Страви: {greedy_result[0]}, вартість: {greedy_result[1]}, калорії: {greedy_result[2]}")

    print("Динамічне програмування:")
    print(f"Страви: {dp_result[0]}, вартість: {dp_result[1]}, калорії: {dp_result[2]}")


if __name__ == "__main__":
    demo()
