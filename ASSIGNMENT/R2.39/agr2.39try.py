from abc import ABC, abstractmethod  # need these definitions


class Polygon(ABC):

    def __init__(self, lengths_of_sides):
        self.number_of_sides = len(lengths_of_sides)
        self.lengths_of_sides = [0] * self.number_of_sides
        self.assign_values_to_sides(lengths_of_sides)

    def print_num_sides(self):
        """a quick, informational print statement"""
        print('There are ' + str(self.number_of_sides) + 'sides.')

    def assign_values_to_sides(self, lengths_of_sides):
        index = 0
        while index < len(lengths_of_sides):
            self.lengths_of_sides[index] = lengths_of_sides[index]
            index += 1

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 3, self.number_of_sides

    def area(self):
        """return the area of the triangle using the semi-perimeter method"""
        a, b, c = self.lengths_of_sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        s = (self.lengths_of_sides[0] + self.lengths_of_sides[1] + self.lengths_of_sides[2])
        return s


class IsoscelesTriangle(Triangle):

    def __init__(self, side, base):  # [side, base]
        super().__init__([side, side, base])


class EquilateralTriangle(Triangle):

    def __init__(self, side):  # side
        super().__init__([side, side, side])


class Pentagon(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 5, self.number_of_sides

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x + y) * 2


class Hexagon(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 6, self.number_of_sides

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x + y) * 2


class Octagon(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        assert 8, self.number_of_sides

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x + y) * 2


class Quadrilateral(Polygon):

    def __init__(self, lengths_of_sides):  # [side1, side2]
        super().__init__([lengths_of_sides[0], lengths_of_sides[1], lengths_of_sides[0], lengths_of_sides[1]])
        assert 4, self.number_of_sides

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x + y) * 2


class Rectangle(Quadrilateral):

    def __init__(self, lengths_of_sides):  # [side1, side2]
        super().__init__(lengths_of_sides)

    def area(self):
        x, y = self.lengths_of_sides[0], self.lengths_of_sides[1]
        return x * y

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        x, y = self.lengths_of_sides
        return (x + y) * 2


class Square(Rectangle):

    def __init__(self, side):
        super().__init__([side, side])

    def area(self):
        x = self.lengths_of_sides[0]
        return x * x

    def perimeter(self):
        """Return the perimeter of the polygon."""
        # calculate the perimeter
        x = self.lengths_of_sides[0]
        return x * 4
