""""
GLLAguilar
    DATALOG Lab04
    FEB. 12, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
from abc import ABC, abstractmethod


class Polygon(ABC):

    def __init__(self, lengths_sides):
        self.number_sides = len(lengths_sides)
        self.lengths_sides = [0] * self.number_sides
        self.assign_values_to_sides(lengths_sides)

    def print_num_sides(self): # defines and prints the number of sides.
        print('There are ' + str(self.number_sides) + 'sides.')

    def assign_values_to_sides(self, lengths_sides):
        index = 0
        while index < len(lengths_sides):
            self.lengths_sides[index] = lengths_sides[index]
            index += 1

    @abstractmethod # Composes of multiple abstract methods.
    def area(self):
        pass

    @abstractmethod
    def perimeter(self): # Composes of multiple abstract methods.
        pass


class Triangle(Polygon):

    def __init__(self, lengths_sides):
        super().__init__(lengths_sides)
        assert 3, self.number_sides

    def area(self): #return the area of the triangle using the semi-perimeter method.
        a, b, c = self.lengths_sides # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def perimeter(self): # Return the perimeter of the polygon.
        s = (self.lengths_sides[0] + self.lengths_sides[1] + self.lengths_sides[2]) # calculate the perimeter.
        return s

class EquilateralTriangle(Triangle):

    def __init__(self, side):
        super().__init__([side, side, side])


class Pentagon(Polygon):

    def __init__(self, lengths_sides):
        super().__init__(lengths_sides)
        assert 5, self.number_sides

    def area(self):
        x, y = self.lengths_sides[0], self.lengths_sides[1]
        return x * y

    def perimeter(self): # Return the perimeter of the polygon.
        x, y = self.lengths_sides # calculate the perimeter
        return (x + y) * 2


class Hexagon(Polygon):

    def __init__(self, lengths_sides):
        super().__init__(lengths_sides)
        assert 6, self.number_sides

    def area(self):
        x, y = self.lengths_sides[0], self.lengths_sides[1]
        return x * y

    def perimeter(self): # Return the perimeter of the polygon.
        x, y = self.lengths_sides # calculate the perimeter
        return (x + y) * 2

class Quadrilateral(Polygon):

    def __init__(self, lengths_sides):  # [side1, side2]
        super().__init__([lengths_sides[0], lengths_sides[1], lengths_sides[0], lengths_sides[1]])
        assert 4, self.number_sides

    def area(self):
        x, y = self.lengths_sides[0], self.lengths_sides[1]
        return x * y

    def perimeter(self): # Return the perimeter of the polygon.
        x, y = self.lengths_sides # calculate the perimeter
        return (x + y) * 2


class Rectangle(Quadrilateral):

    def __init__(self, lengths_sides):  # [side1, side2]
        super().__init__(lengths_sides)

    def area(self):
        x, y = self.lengths_sides[0], self.lengths_sides[1]
        return x * y

    def perimeter(self): # Return the perimeter of the polygon.
        x, y = self.lengths_sides # calculate the perimeter
        return (x + y) * 2


class Square(Rectangle):

    def __init__(self, side):
        super().__init__([side, side])

    def area(self):
        x = self.lengths_sides[0]
        return x * x

    def perimeter(self): # Return the perimeter of the polygon.
        x = self.lengths_sides[0] # # calculate the perimeter
        return x * 4

if __name__ == "__main__":

    number_sides = 5
    lengths_sides = 23