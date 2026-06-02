"""Завдання 2. Рекурсивне створення фрактала «дерево Піфагора»."""

from __future__ import annotations
import argparse
import math
import matplotlib.pyplot as plt


def draw_pythagoras_tree(
    ax: plt.Axes,
    x: float,
    y: float,
    length: float,
    angle: float,
    level: int,
) -> None:
    """Рекурсивно малює фрактал дерева Піфагора."""
    if level == 0:
        return

    x_end = x + length * math.cos(math.radians(angle))
    y_end = y + length * math.sin(math.radians(angle))

    ax.plot([x, x_end], [y, y_end], linewidth=max(level / 2, 0.5))

    next_length = length * 0.7
    draw_pythagoras_tree(ax, x_end, y_end, next_length, angle + 45, level - 1)
    draw_pythagoras_tree(ax, x_end, y_end, next_length, angle - 45, level - 1)


def visualize_tree(level: int) -> None:
    """Створює вікно з фракталом для заданого рівня рекурсії."""
    if level < 0:
        raise ValueError("Рівень рекурсії не може бути від'ємним")

    fig, ax = plt.subplots(figsize=(8, 8))
    draw_pythagoras_tree(ax, 0, 0, 1.0, 90, level)
    ax.set_title(f"Дерево Піфагора. Рівень рекурсії: {level}")
    ax.set_aspect("equal")
    ax.axis("off")
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(description="Візуалізація фрактала 'дерево Піфагора'.")
    parser.add_argument("level", nargs="?", type=int, help="Рівень рекурсії")
    args = parser.parse_args()

    level = args.level
    if level is None:
        level = int(input("Введіть рівень рекурсії: "))

    visualize_tree(level)


if __name__ == "__main__":
    main()
