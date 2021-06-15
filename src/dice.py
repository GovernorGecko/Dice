"""
    Dice.py
"""

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

        # Go either side of our count, comparing averages
        # and taking the closest.
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

    def roll(self):
        """
        returns:
            List of Integers
        """

        # Roll results!
        roll_results = []

        # Create em!
        for _ in range(0, self.__count):
            roll_results.append(random.choice(range(1, self.__sides + 1)))

        # Return
        return roll_results

    def roll_drop_lowest(self, count=1):
        """
        parameters:
            Int of lowest to drop
        returns:
            List of Int rolls
        """

        # Error checking
        if (
            not isinstance(count, int) or
            count < 0 or
            count >= self.__count
        ):
            raise ValueError(
                f"Count must be an integer,"
                f"greater than 0 and less than {self.__count}"
            )

        # Roll results!
        roll_results = self.roll()

        # Iterate!
        for _ in range(0, count):
            roll_results.remove(min(roll_results))

        # Return
        return roll_results

    def roll_sum(self):
        """
        returns:
            int of our rolls, added together.
        """

        # Get the results!
        roll_results = self.roll()

        # Return!
        return sum(roll_results)

    def roll_sum_drop_lowest(self, count=0):
        """
        parameters:
            Int of lowest to drop
        returns:
            Int sum of rolls
        """

        # Get the resutls!
        roll_results = self.roll_drop_lowest(count)

        # Return!
        return sum(roll_results)

    def roll_sum_with_culling(
        self, minimum=None, maximum=None, lowest_to_drop=0
    ):
        """
        parameters:
            Int/None minimum number to accept
            Int/None maximum number to accept
            Int lowest numbers to drop
        returns:
            Int sum of our rolls, after culling.
        """

        # Get the sum of our roll, dropping the lowest.
        roll_sum = self.roll_sum_drop_lowest(lowest_to_drop)

        # Minimum?
        if minimum is not None and roll_sum < minimum:
            return minimum
        # Maximum?
        elif maximum is not None and roll_sum > maximum:
            return maximum

        # We good!
        return roll_sum
