#!/usr/bin/env python3

"""A basic greedy algorithim to solve the multidimensional 0–1 knapsack problem


Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi1@marist.edu>
"""


class GreedyAlgorithm:
    """Basic Greedy Algorithim
    
    Attributes
    ----------
    knapsacks : List[list]
        all knapsacks in a list
    """

    def __init__(
        self, objects: list, knapsacks: int, capacity: int, average_value: int
    ):
        """
        Parameters
        ----------
        objects : list
            elements to be stored in a knapsack
        knapsacks : int
            number of knapsacks
        capacity : int
            how much a knapsack can hold
        average_value : int
            average of all object values
        """
        self.num_of_knapsacks = knapsacks
        self.capacity = capacity
        self.__average_value = average_value
        self.__objects = objects
        self.__knapsacks = [[None for x in range(capacity)] for y in range(knapsacks)]
        self.used_objects = []
        self.fillKnapsacks()

    @property
    def knapsacks(self):
        return self.__knapsacks

    @knapsacks.setter
    def knapsacks(self, knapsack):
        self.__knapsacks = knapsack

    def append(self, val):
        self.knapsacks = self.knapsacks + [val]
        return self.knapsacks

    def fillKnapsacks(self):
        """goes through all objects and fills each knapsack with the best choice at the time """
        adding_objects = True
        object_index = 0
        knapsack_index = 0
        loop = 0
        while adding_objects:
            self.knapsacks[knapsack_index][object_index] = self.__objects.pop(0)

            if knapsack_index is self.num_of_knapsacks - 1:
                object_index += 1
                loop += 1
                knapsack_index = 0
                if loop is self.capacity:
                    adding_objects = False
            else:
                knapsack_index += 1
