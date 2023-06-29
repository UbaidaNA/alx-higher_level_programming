#!/usr/bin/python3

"""
This class defines a square.
"""

class Square:
    """
    This class represents a square.
    """

    def __init__(self, size)
        """
        Initializes a new square

        Args:
            size (int): Size of new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
