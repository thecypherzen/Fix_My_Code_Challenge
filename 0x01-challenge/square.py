#!/usr/bin/python3
"""A class that defines a square"""


class square():
    """ Defines a square

    Class Attributes:
        width(int): width of square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initializes the square class

        args(obj:tuple): list of arguments
        kwargs(:obj:dict): dictionary of keyword arguments
        """
        if "width" in kwargs.keys():
            setattr(self, "width", kwargs["width"])
            setattr(self, "height", kwargs["width"])

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Calculates peremiter of square """
        return (self.width * 4)

    def __str__(self):
        """ Creates string representation of square """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
    print(s.width, s.height)
