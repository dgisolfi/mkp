#!/usr/bin/env python3

"""A generic object to hold a users data for sorting


Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi1@marist.edu>
"""


class Object:
    def __init__(self, title, value, **kwargs):
        """basic object for sorting
        
        Parameters
        ----------
        title : str
            title of object for reference
        value : int
        """
        self.__title = title
        self.__value = value

    def __repr__(self):
        return f"{self.__title}-{self.__value}"

    @property
    def title(self):
        return self.__title

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val
