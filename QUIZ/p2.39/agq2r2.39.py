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

    class Pentagon(lengths_sides):

        def __init__(self, lengths_sides):
            super().__init__(lengths_sides)
            assert 5, self.number_sides

        def area(self):
            x, y = self.lengths_sides[0], self.lengths_sides[1]
            return x * y

        def perimeter(self):  # Return the perimeter of the polygon.
            x, y = self.lengths_sides  # calculate the perimeter
            return (x + y) * 2


    class Hexagon(lengths_sides):

        def __init__(self, lengths_sides):
            super().__init__(lengths_sides)
            assert 6, self.number_sides

        def area(self):
            x, y = self.lengths_sides[0], self.lengths_sides[1]
            return ((3 * math.sqrt(3) *
            (s * s)) / 2)

        def perimeter(self):  # Return the perimeter of the polygon.
            x, y = self.lengths_sides  # calculate the perimeter
            return (x + y) * 2

if __name__=="__main__":
    lengths_sides = 4

    print("Area:", "{0:.4f}".
          format(Hexagon(lengths_sides)))