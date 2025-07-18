"""
Dice.py
"""

import copy
import itertools
import math
import operator
import random
from typing import Callable


class Dice:
    """
    Doice!

    Can add Dice into the constructur with Tuples or single Ints.
    Tuples  =   (Sides, Count)
    Int     =   Sides
    """

    __slots__ = ["__dice"]

    def __init__(self, *dice):
        self.__dice: dict[int, int]
        self.__dice = {}

        if dice:
            for die in dice:
                if isinstance(die, int):
                    self.add_die(die)
                elif (
                    isinstance(die, tuple)
                    and len(die) == 2
                    and isinstance(die[0], int)
                    and isinstance(die[1], int)
                ):
                    self.add_die(die[0], die[1])

    def __str__(self) -> str:
        """
        {count}d{sides}
        """

        return " ".join(f"{count}d{sides}" for sides, count in self.get_dice().items())

    def __add__(self, other):
        """
        Adds two sets of Dice together, returning a new Dice object.
        """

        if isinstance(other, Dice):
            dice_copy: Dice = copy.deepcopy(self)

            other: Dice
            for sides, count in other.get_dice().items():
                dice_copy.add_die(sides, count)

            return dice_copy

        return self

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
            all_die_sides.append([(i + 1) for i in range(die_sides)])

        return list(itertools.product(*all_die_sides))

    def get_average(self) -> float:
        """
        The average for Rolls.
        """

        total_average: float = 0.0

        for sides, count in self.get_dice().items():
            total_average += (((float(sides) - 1.0) / 2.0) + 1.0) * float(count)

        return total_average

    def get_dice(self) -> dict[int, int]:
        """
        Returns our dice dictionary, sorted by size
        """

        return dict(sorted(self.__dice.items()))

    def get_die_sides(self) -> list[int]:
        """
        Returns sides of each die
        """

        die_sides: list[int] = []

        for sides, count in self.get_dice().items():
            die_sides.extend([sides] * count)

        return die_sides

    def get_max_roll(self) -> int:
        """
        Returns max possible roll
        """

        return sum([sides * count for sides, count in self.get_dice().items()])

    def get_min_roll(self) -> int:
        """
        Returns min possible roll
        """

        return sum([count for count in self.get_dice().values()])

    def get_probability_outcome(self) -> int:
        """
        Probability outcome is sides * sides...
        """

        return math.prod(self.get_die_sides())

    def _get_probability_sum_with_operator(self, oper: operator, value: int) -> float:
        """
        Handles probability math, given an operator (greater than...)
        """

        if not isinstance(value, int):
            raise ValueError("Value must be an int.")

        total_possibilities = 0

        for possibility in self.get_all_possible_rolls():
            if oper(sum(possibility), value):
                total_possibilities += 1

        return total_possibilities / self.get_probability_outcome()

    def get_probability_sum_equals(self, value: int) -> float:
        """
        Probability we roll equal given sum
        """

        return self._get_probability_sum_with_operator(operator.eq, value)

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

        for sides, count in self.get_dice().items():
            rolls[sides] = [random.choice(range(1, sides + 1)) for _ in range(count)]

        return rolls

    def roll_sum(self) -> int:
        """
        Rolls and returns the sum of the roll.
        """

        return sum(self.roll())


D4 = Dice(4)
D6 = Dice(6)
D8 = Dice(8)
D10 = Dice(10)
D12 = Dice(12)
D20 = Dice(20)


def dice_roll_drop(
    sides: int, count: int, drop_func: Callable[[list[int]], int]
) -> tuple[list[int], int]:
    """
    Roll count dice of size, dropping based off passed in func.
    """

    if not isinstance(sides, int) or sides < 1:
        raise ValueError(f"Sides must be an integer and greater than 0")
    elif not isinstance(count, int) or count < 1:
        raise ValueError(f"Count must be an integer and greater than 0")

    dice = Dice()
    dice.add_die(sides, count)

    roll_results = dice.roll()
    highest_roll = drop_func(roll_results)
    roll_results.remove(highest_roll)

    return (roll_results, highest_roll)


def dice_roll_drop_highest(sides: int, count: int = 1) -> tuple[list[int], int]:
    """
    Roll count dice of size, dropping the highest roll.
    """

    return dice_roll_drop(sides, count, max)


def dice_roll_drop_lowest(sides: int, count: int = 1) -> tuple[list[int], int]:
    """
    Roll count dice of size, dropping the lowest roll.
    """

    return dice_roll_drop(sides, count, min)


def dice_roll_sum_drop_highest(sides: int, count: int) -> int:
    """
    Rolls and drops the highest value given sides and count.
    Returns the sum of the roll.
    """

    return sum(dice_roll_drop_highest(sides, count)[0])


def dice_roll_sum_drop_lowest(sides: int, count: int) -> int:
    """
    Rolls and drops the lowest value given sides and count..
    Returns the sum of the roll.
    """

    return sum(dice_roll_drop_lowest(sides, count)[0])
