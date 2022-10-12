#!/usr/bin/python3

"""Square module"""

class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initializes square objects
        Args:
                size: Length of a square.
        Raises:
                TypeError: When size is not an integer
                ValueError: When size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
