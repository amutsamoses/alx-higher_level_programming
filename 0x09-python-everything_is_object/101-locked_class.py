#!/usr/bin/python3
""" Locked Class
"""


class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("Cannot set attribute")
        super().__setattr__(name, value)
