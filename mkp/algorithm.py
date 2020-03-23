#!/usr/bin/env python3
"""
"""


class GreedyAlgorithm:
    def __init__(
        self, objects: list, knapsacks: int, knapsack_size: int, average_value
    ):
        self.num_of_knapsacks = knapsacks
        self.knapsack_size = knapsack_size
        self.__average_value = average_value
        self.__objects = objects
        self.__knapsacks = [
            [None for x in range(knapsack_size)] for y in range(knapsacks)
        ]
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
                if loop is self.knapsack_size:
                    adding_objects = False
            else:
                knapsack_index += 1
