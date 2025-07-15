"""
Dice Examples
"""

from src.dice import (
    Dice,
    Die,
    dice_roll_drop_highest,
    dice_roll_drop_lowest,
    dice_roll_sum_drop_highest,
    dice_roll_sum_drop_lowest,
)

print("Die Examples")
die = Die(4)
print(die)
print(die.get_average())
print(die.get_all_possible_rolls())
print(die.roll())

print("\nDice Examples")
dice = Dice()
dice.add_die(4, 2)
dice.add_die(6, 1)
print(dice)
print(dice.get_average())
print(dice.roll_detail())
print(dice.roll())
print(dice.roll_sum())
print(dice.get_die_sides())
# print(dice.get_all_possible_rolls())
print(dice.get_probability_sum_greater_than(6))
print(dice.get_probability_sum_less_than(7))
print(dice.get_probability_sum_equals(10))

print("\nStatic Func Examples")
print(dice_roll_drop_highest(20, 4))
print(dice_roll_drop_lowest(20, 4))
print(dice_roll_sum_drop_highest(20, 4))
print(dice_roll_sum_drop_lowest(20, 4))
