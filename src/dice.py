"""
    Dice.py
"""

# Sys
import array
import math
import random


class Dice:
    """
    Doice!
    parameters:
        int sides
        int count
        int bonus
    """

    # Valid sides for our dice.
    __valid_sides = [2, 4, 6, 8, 10, 12, 20, 100]

    __slots__ = ["__bonus", "__count", "__sides"]

    def __init__(self, sides, count=1, bonus=0):

        # Validate data
        if (
            not isinstance(sides, int) or
            not isinstance(count, int) or
            not isinstance(bonus, int)
        ):
            raise ValueError("Expected Integer for Sides, Count, and Bonus.")
        elif sides not in self.__valid_sides:
            raise ValueError(f"Given sides not in {self.__valid_sides}")

        # Store vars
        self.__bonus = bonus
        self.__count = count if count > 0 else 1
        self.__sides = sides

    def __str__(self):
        """
        returns:
            str representation of this Dice
        """

        return f"{self.__count}d{self.__sides}"

    def get_average(self):
        """
        returns:
            float average of this Dice
        """

        # Average
        average = (((self.__sides - 1) / 2) + 1) * self.__count

        # Return
        return average + self.__bonus

    def get_scaled(self, scale=1):
        """
        parameters:
            int value to scale by.  This is how many sizes up/down
            to scale.
        returns:
            Dice scaled to scale
        """

        # Error?
        if not isinstance(scale, int):
            raise ValueError("Scale must be an int.")

        # Scaled dice to return!
        scaled_dice = self

        # Which direction we going?
        if scale > 0:
            for _ in range(0, scale):
                scaled_dice = scaled_dice.get_scaled_adjacent(1)
        elif scale < 0:
            for _ in range(scale, 0):
                scaled_dice = scaled_dice.get_scaled_adjacent(-1)

        # Return the scaled dice!
        return scaled_dice        

    def get_scaled_adjacent(self, direction=1):
        """
        parameters:
            int direction, 1 or -1
        returns:
            Dice of our scaled.
        """

        # Valid parameter?
        if (
            not isinstance(direction, int) or
            direction not in [-1, 1]
        ):
            raise ValueError("Direction must be 1 or -1.")

        # Min/Max of count.
        minimum_count = self.__count - 5
        if minimum_count < 0:
            minimum_count = 0
        maximum_count = self.__count + 5 

        # Go either side of our count, comparing averages and taking the closest.
        closest_dice = None
        for count in range(minimum_count, maximum_count):
            for sides in self.__valid_sides:
                average = Dice(sides, count).get_average()                  
                if (
                    (
                        direction == 1 and
                        average > self.get_average() and
                        (
                            closest_dice is None or
                            average < closest_dice.get_average()
                        )
                    ) or
                    (
                        direction == -1 and
                        average < self.get_average() and
                        (
                            closest_dice is None or
                            average > closest_dice.get_average()
                        )
                    )
                ):
                    closest_dice = Dice(sides, count)
        
        # Return
        return closest_dice

    def roll(self, count_to_return=-1, drop_lowest=True):
        """
        Roll them bones!
        """

        # No count?  Set as self.
        if count_to_return == -1:
            count_to_return = self.__count

        # Prepared the die range.  Starts at 1, < number_of_sides + 1.
        die_range = range(1, (self.__sides + 1))

        # Array of die rolls
        dice_rolls = array.array('I')

        # Perform the rolls, may the odds ever be in your favor!
        for _ in range(0, self.__count):
            dice_rolls.insert(0, random.choice(die_range))

        # Start dropping dice!
        while len(dice_rolls) > count_to_return:

            # We want min or max?
            dice_rolls_search = min(dice_rolls)
            if not drop_lowest:
                dice_rolls_search = max(dice_rolls)

            # Now get the first index of the value and remove it!
            dice_rolls.pop(dice_rolls.index(dice_rolls_search))

        # Return it!
        return dice_rolls

    def roll_single(self):
        """
        Rolls and returns a single die roll
        """

        # Array of Dice Rolls
        dice_rolls = self.roll()

        # Just return the first single.
        return dice_rolls[0]

    def roll_sum(
        self, sets_to_roll, maximum=None,
        minimum=None, count_to_return=1,
        drop_lowest=True
    ):
        """
        Builds an array of Dice Rolls, given criteria.
        """

        # Array of Dice Rolls
        dice_rolls = array.array('I')

        # Iterate Dice Rolls
        for _ in range(0, sets_to_roll):

            # Roll the dice!
            dice_rolled = self.roll(count_to_return, drop_lowest)

            # Sum it!
            dice_rolled_sum = sum(dice_rolled)

            # Need to Max/Min?
            if maximum is not None and dice_rolled_sum > maximum:
                dice_rolled_sum = maximum
            elif minimum is not None and dice_rolled_sum < minimum:
                dice_rolled_sum = minimum

            # Insert!
            dice_rolls.insert(0, dice_rolled_sum)

        # Returnnn!
        return dice_rolls

    def roll_sum_list(
        self, sets_to_roll, maximum=None,
        minimum=None, count_to_return=1,
        drop_lowest=True
    ):
        """
        Returns alist of the sum roll
        """

        return self.roll_sum(
            sets_to_roll, maximum, minimum,
            count_to_return, drop_lowest
        ).tolist()

    def roll_sum_single(self):
        """
        We only need a single result?  Just returns the Integer
        """

        # Array of Dice Rolls
        dice_rolls = self.roll_sum(1)

        # Just return the first single.
        return dice_rolls[0]

    def update(self, sides=None, count=None):
        """
        Update our values
        """

        if sides:
            self.__sides = sides
        if count:
            self.__count = count

