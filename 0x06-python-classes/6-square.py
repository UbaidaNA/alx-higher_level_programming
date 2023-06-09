#!/usr/bin/python3

"""
This class defines a square.
"""

class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square

        Args:
            size (int): Size of new square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self, value):
        """
        Set the current size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

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

    def my_print(self):
        """
        Print the square with the '#' character
        Print an empty line if size is 0        
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
