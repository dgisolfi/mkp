#!/usr/bin/env python3
"""
"""


class GreedyAlgorithm:
    def __init__(self, objects: list, knapsacks: int, team_size: int, average_value):
        self.__objects = objects
        self.__teams = [[None for x in range(team_size)] for y in range(knapsacks)]
        self.__average_value = average_value
        self.used_objects = []
        self.fillKnapsacks()

    @property
    def teams(self):
        return self.__teams

    @teams.setter
    def teams(self, team):
        self.__teams = team

    def append(self, val):
        self.teams = self.teams + [val]
        return self.teams

    def fillKnapsacks(self):
        adding_objects = True
        player_index = 0
        team_index = 0
        loop = 0
        while adding_objects:
            self.teams[team_index][player_index] = self.__objects.pop(0)

            if team_index is 4:
                player_index += 1
                loop += 1
                team_index = 0
                if loop is 3:
                    adding_objects = False
            else:
                team_index += 1
