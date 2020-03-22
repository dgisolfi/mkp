#!/usr/bin/env python3
# 2019-5-5

import re
import sys

from mkp.object import Object


class Parser:
    def __init__(self, filename):
        self.filename = filename
        self.__commands = []
        self.__avg_value = 0
        self.__objects = []
        self.parse()

    @property
    def commands(self):
        return self.__commands

    @property
    def avg_value(self):
        return self.__avg_value

    @avg_value.setter
    def avg_value(self, avg_value):
        self.__avg_value = avg_value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, objs):
        self.__objects = objs

    def getCmds(self, filename):
        try:
            file = open(filename, "r")
            commands = file.readlines()
            file.close()
            return commands
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def clean(self):
        self.__commands = [re.sub(r"\n", "", line) for line in self.__commands]
        self.__commands = [re.sub(r"^--.*$", "", line) for line in self.__commands]
        self.__commands = [i for i in self.__commands if i]

    def parse(self):
        # Get all commands from the file
        self.__commands = self.getCmds(self.filename)
        # Remove the comments and line breaks from the commands
        self.clean()

        total_value = 0
        # parse all spices and knapsacks
        for cmd in self.commands:
            elements = cmd.strip().split(";")
            elements = [i for i in elements if i]
            self.objects.append(
                Object(
                    elements[0], sum(int(num) for num in elements[1 : len(elements)])
                )
            )
            total_value += self.objects[-1].value

        self.avg_value = total_value // len(self.objects)
