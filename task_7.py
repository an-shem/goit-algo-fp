"""Завдання 7. Метод Монте-Карло для кидання двох кубиків."""

from __future__ import annotations
from collections import Counter
import random
import matplotlib.pyplot as plt

ANALYTICAL_PROBABILITIES = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def monte_carlo_dice_simulation(rolls: int = 100_000) -> dict[int, float]:
    """Імітує кидання двох кубиків і повертає ймовірності сум."""
    if rolls <= 0:
        raise ValueError("Кількість кидків має бути більшою за нуль")

    counter: Counter[int] = Counter()

    for _ in range(rolls):
        first_die = random.randint(1, 6)
        second_die = random.randint(1, 6)
        counter[first_die + second_die] += 1

    return {dice_sum: counter[dice_sum] / rolls for dice_sum in range(2, 13)}


def print_probability_table(simulated_probabilities: dict[int, float]) -> None:
    """Виводить таблицю порівняння ймовірностей."""
    print("Сума | Монте-Карло | Аналітично | Різниця")
    print("-----|-------------|------------|---------")

    for dice_sum in range(2, 13):
        simulated = simulated_probabilities[dice_sum]
        analytical = ANALYTICAL_PROBABILITIES[dice_sum]
        difference = abs(simulated - analytical)
        print(f"{dice_sum:>4} | {simulated * 100:>10.2f}% | {analytical * 100:>9.2f}% | {difference * 100:>6.2f}%")


def plot_probabilities(simulated_probabilities: dict[int, float]) -> None:
    """Будує графік порівняння ймовірностей."""
    sums = list(range(2, 13))
    simulated = [simulated_probabilities[dice_sum] * 100 for dice_sum in sums]
    analytical = [ANALYTICAL_PROBABILITIES[dice_sum] * 100 for dice_sum in sums]

    plt.figure(figsize=(10, 6))
    plt.plot(sums, simulated, marker="o", label="Метод Монте-Карло")
    plt.plot(sums, analytical, marker="s", label="Аналітичні розрахунки")
    plt.title("Порівняння ймовірностей сум двох кубиків")
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність, %")
    plt.xticks(sums)
    plt.grid(True)
    plt.legend()
    plt.show()


def main() -> None:
    rolls = 100_000
    probabilities = monte_carlo_dice_simulation(rolls)
    print(f"Кількість кидків: {rolls}")
    print_probability_table(probabilities)
    plot_probabilities(probabilities)


if __name__ == "__main__":
    main()
