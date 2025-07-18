"""
_examples.py
Dice Examples
"""

from src.dice import (
    Dice,
    D4,
    dice_roll_drop_highest,
    dice_roll_drop_lowest,
    dice_roll_sum_drop_highest,
    dice_roll_sum_drop_lowest,
)

print("\n -- Build Dice --")
dice = Dice((12, 1), 6)
dice.add_die(6, 1)
dice += D4
dice += Dice(8)

print("\n -- Dice Data --")
print(f"str()\t\t{dice}")
print(f"git_dice()\t{dice.get_dice()}")
print(f"get_average()\t{dice.get_average()}")
print(f"get_max_roll()\t{dice.get_max_roll()}")
print(f"get_min_roll()\t{dice.get_min_roll()}")

print("\n -- Dice Rolls --")
print(f"roll()\t\t{dice.roll()}")
print(f"roll_detail()\t{dice.roll_detail()}")
print(f"roll_sum()\t{dice.roll_sum()}")

print("\n -- Dice Probability --")
print(f"get_die_sides()\t\t\t\t{dice.get_die_sides()}")
print(
    f"get_probability_sum_greater_than(6)\t{dice.get_probability_sum_greater_than(6)}"
)
print(f"get_probability_sum_less_than(7)\t{dice.get_probability_sum_less_than(7)}")
print(f"get_probability_sum_equals(10)\t\t{dice.get_probability_sum_equals(10)}")

print("\n -- Static Func Examples -- ")
print(f"dice_roll_drop_highest(20, 2)\t\t{dice_roll_drop_highest(20, 2)}")
print(f"dice_roll_drop_lowest(20, 2))\t\t{dice_roll_drop_lowest(20, 2)}")
print(f"dice_roll_sum_drop_highest(20, 2)\t{dice_roll_sum_drop_highest(20, 2)}")
print(f"dice_roll_sum_drop_lowest(20, 2)\t{dice_roll_sum_drop_lowest(20, 2)}")
