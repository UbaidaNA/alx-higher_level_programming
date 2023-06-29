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

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
               len(value) != 2 or
               not all(isinstance(num, int) for num in value) or
               not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

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
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
