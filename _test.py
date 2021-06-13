"""
Dice Tests
"""

from src.dice import Dice

d = Dice(2, 2)

print(d.get_average())
print(d.get_scaled(1))
