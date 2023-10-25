#!/usr/bin/bash/python3

""" a class Square that defines a square by: (based on 0-square.py)"""
class Square:
    """Private instance attribute: size
    Instantiation with size (no type/value verification)"""
    def __init__(self, size):
        """Initializes the size of the square
        size is a private attribute
        Arguement:
            size(int) return integer value of the square"""
        self.__size = size 
        """__size field that stores the value and size is value provided when
        i create the object"""
