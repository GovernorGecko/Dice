"""
Dice Tests
"""

from src.dice import Dice

d = Dice(4, 3)

print(d.get_average())
print(d.get_scaled(2))
print(d.get_scaled(2).get_average())
print(d)


"""
    Handles rolling of dice!
    # Dice Progression
    # Dice					Mean		Max		Min
    DICE_PROGRESSION = [
        Dice(4, 1),		# 2.5		4		1
        Dice(2, 2),		# 3			4		2
        Dice(6, 1), 	# 3.5		6		1
        Dice(3, 2),		# 4			6		2
        Dice(8, 1),		# 4.5		8		1
        Dice(4, 2),		# 5			8		2
        Dice(10, 1),    # 5.5		10		1
        Dice(5, 2),		# 6			10		2
        Dice(12, 1),    # 6.5		12		1
        Dice(6, 2),		# 7			12		2
        Dice(4, 3),		# 7.5		12		3
        Dice(8, 2),		# 9			16		2
        Dice(4, 4),		# 10			16		4
        Dice(6, 3),		# 10.5		18		3
        Dice(20, 1),    # 10.5		20		1
        Dice(3, 6)		# 12			18		6
    ]
# Valid Sides as Dice, 1 Count, no Bonus
dice_valid_sides = []
for sides in self.__valid_sides:
    dice_valid_sides.append(
        Dice(sides)
    )

# Expected Average
expected_average = self.get_average() + scale

# This average valid?
while expected_average <= 0.0:
    expected_average += 1.0          

# Dice Scaled to return.
dice_scaled = Dice(
    self.__sides, self.__count, self.__bonus
)  

# Go for the Average!
direction = 1 if scale > 0 else -1
step = self.__count
while dice_scaled.get_average() != expected_average:
    for sides in self.__valid_sides:
        dice = Dice(sides, step, self.__bonus)
        if dice.get_average() == expected_average:
            print(dice)
            dice_scaled.update(sides, step)
    step += direction
        
# Return the Scaled Dice
return dice_scaled

"""

"""
# Scale set at 0?
if scale != 0:

    # First, find out which DICE_PROGRESSION we are at.
    for i in range(0, len(DICE_PROGRESSION)):

        # Store the dice
        d = DICE_PROGRESSION[i]

        # This us?
        if d.__count == self.__count and d.__sides == self.__sides:

            # Found us?  Nice!
            d_scale_index = i + scale

            # This exist?
            if d_scale_index < len(DICE_PROGRESSION):

                # Grab
                d_scale = DICE_PROGRESSION[d_scale_index]

                # Return the scaled version!
                return Dice(d_scale.__sides, d_scale.__count)

# Couldn't find or scale, pass a copy of our original.
return Dice(self.__sides, self.__count)
"""