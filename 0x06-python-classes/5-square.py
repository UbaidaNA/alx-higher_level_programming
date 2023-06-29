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
        self.size = size

    @property
    def size(self):
        """
        Set the cureent size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the current square
        """
        return (self.__size ** 2)

    def my_print:
        """
        Print the square with the '#' character
        """
        for i in range(0, self.__size):
            [print("#", end="")for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
