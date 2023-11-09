#!/usr/bin/python3
"""MyList inherits from the list class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list  but sorted (ascending sort)"""
        print(sorted(self))
