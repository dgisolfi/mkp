#!/usr/bin/env python3

"""Parses the lines of a given file


Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi1@marist.edu>
"""

import re
import sys

from typing import List
from mkp.object import Object


class Parser:
    """parses a file
    
    Attributes
    ----------
    lines : List[str]
        lines of the file given file
    avg_value : int
        the average value of each object
    objects : List[Objects]
        a list of the read in objects
    """

    def __init__(self, path: str):
        self.path = path
        self.__lines = []
        self.__avg_value = 0
        self.__objects = []
        self.parse()

    @property
    def lines(self):
        return self.__lines

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

    def read(self, path: str) -> List[str]:
        """reads all lines in from a file
        
        Parameters
        ----------
        path : str
            path to the file
        
        Returns
        -------
        List[str]
            all lines of the file
        """
        try:
            file = open(self.path, "r")
            lines = file.readlines()
            file.close()
            return lines
        except Exception as e:
            print(f"🎒 Error: {e}")
            sys.exit(1)

    def clean(self):
        """cleans all commments, empty lines and line breaks from the data """
        self.__lines = [re.sub(r"\n", "", line) for line in self.__lines]
        self.__lines = [re.sub(r"^--.*$", "", line) for line in self.__lines]
        self.__lines = [i for i in self.__lines if i]

    def parse(self):
        """ Creates all data as Objects to be used by the algorithim """
        # Get all lines from the file
        self.__lines = self.read(self.path)
        # Remove the comments and line breaks from the lines
        self.clean()

        total_value = 0
        # parse all spices and knapsacks
        for cmd in self.lines:
            elements = cmd.strip().split(";")
            elements = [i for i in elements if i]
            self.objects.append(
                Object(
                    elements[0], sum(int(num) for num in elements[1 : len(elements)])
                )
            )
            total_value += self.objects[-1].value

        self.avg_value = total_value // len(self.objects)
