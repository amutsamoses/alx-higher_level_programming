#!/usr/bin/bash/python3

""" a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""
class Rectangle:

    """Class rectangle"""
    def __init__(self, width = 0, height = 0):

        """inistantiation with optional width and height"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """width"""
            return self.__width

        @property
        def height(self):
            """height"""
            return self.__height

        @width.setter
        def width(self, value):
            """width setter"""

            if type(width) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")

            self.__width = value

        @height.setter
        def height(self, value):
            """height setter"""
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >=0")
            self.__height = value
