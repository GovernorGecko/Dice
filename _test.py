"""
Dice Tests
"""

from src.dice import Dice

d = Dice(4, 3)

print(d)
print(d.get_average())
print(d.get_scaled(2))
print(d.get_scaled(2).get_average())
print(d.roll())
print(d.roll_sum())
print(d.roll_drop_lowest(2))
print(d.roll_sum_with_culling(2, 8, 1))
