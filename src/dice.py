"""
Dice.py
"""

import itertools
import math
import operator
import random


class Die:
    """
    A singular Die
    """

    __slots__ = ["__sides"]

    def __init__(self, sides: int):
        if not isinstance(sides, int):
            raise ValueError("Expected int for Sides")
        self.__sides = sides if sides > 0 else 1

    def __str__(self) -> str:
        """
        d{sides}
        """

        return f"d{self.get_sides()}"

    def get_all_possible_rolls(self) -> list[int]:
        """
        Returns all possible combination of rolls
        """

        return [(i + 1) for i in range(self.get_sides())]

    def get_average(self) -> float:
        """
        The average for this Die.
        """

        return ((float(self.get_sides()) - 1.0) / 2.0) + 1.0

    def get_sides(self) -> int:
        """
        Returns the number of sides
        """

        return self.__sides

    def roll(self) -> list[int]:
        """
        Roll
        """

        return random.choice(range(1, self.get_sides() + 1))


class Dice:
    """
    Doice!
    """

    __slots__ = ["__dice"]

    def __init__(self):
        self.__dice = {}

    def __str__(self) -> str:
        """
        {count}d{sides}
        """

        return " ".join(f"{count}d{sides}" for sides, count in self.__dice.items())

    def add_die(self, sides: int, count: int = 1):
        """
        Given the number of sides of a die, adds/updates its count to our Dice
        """

        if not isinstance(count, int) or count < 1:
            raise ValueError(f"Count must be an integer and greater than 0")
        elif not isinstance(sides, int) or sides < 1:
            raise ValueError(f"Sides must be an integer and greater than 0")

        if sides in self.__dice.keys():
            self.__dice[sides] += count
        else:
            self.__dice[sides] = count

    def get_all_possible_rolls(self) -> list[list[int]]:
        """
        Returns all possible combination of rolls
        """

        all_die_sides: list[list[int]] = []

        for die_sides in self.get_die_sides():
            all_die_sides.append(range(1, die_sides + 1))

        return list(itertools.product(*all_die_sides))

    def get_average(self) -> float:
        """
        The average for Rolls.
        """

        total_average: float = 0.0

        for sides, count in self.__dice.items():
            total_average += Die(sides).get_average() * float(count)

        return total_average

    def get_die_sides(self) -> list[int]:
        """
        Returns sides of each die
        """

        die_sides: list[int] = []

        for sides, count in self.__dice.items():
            die_sides.extend([sides] * count)

        return die_sides

    def get_probability_outcome(self) -> int:
        """
        Probability outcome is sides * sides...
        """

        return math.prod(self.get_die_sides())

    def _get_probability_sum_with_operator(self, oper: operator, value: int) -> float:
        """
        Handles probability math, given an operator (greater than...)
        """

        total_possibilities = 0

        for possibility in self.get_all_possible_rolls():
            if oper(sum(possibility), value):
                total_possibilities += 1

        return total_possibilities / self.get_probability_outcome()

    def get_probability_sum_greater_than(self, value: int) -> float:
        """
        Probability we roll greater than given sum
        """

        return self._get_probability_sum_with_operator(operator.gt, value)

    def get_probability_sum_less_than(self, value: int) -> float:
        """
        Probability we roll less than given sum
        """

        return self._get_probability_sum_with_operator(operator.lt, value)

    def roll(self) -> list[int]:
        """
        Rolls, returning a single array
        """

        return [i for k in self.roll_detail().values() for i in k]

    def roll_detail(self) -> dict[str, list[int]]:
        """
        Rolls, splitting out Dice as keys.
        """

        rolls = {}

        for sides, count in self.__dice.items():
            rolls[f"{count}d{sides}"] = [Die(sides).roll() for _ in range(count)]

        return rolls

    def roll_sum(self) -> int:
        """
        Rolls and returns the sum of the roll.
        """

        return sum(self.roll())
