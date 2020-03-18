from math import tan, pi

class Polygon:

    def __init__(self, lengths_of_sides):
        self._lengths_of_sides = lengths_of_sides

class Pentagon(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)
        self._perimeter = self.perimeter()

    def perimeter(self):
        '''Return the perimeter of the polygon.'''
        # calculate the perimeter
        return (self._lengths_of_sides*5)

    def area(self):
        apothem = self._lengths_of_sides / (2 * tan(pi/5))
        return apothem * self._perimeter / 2


class Hexagon(Polygon):

    def __init__(self, lengths_of_sides):
        super().__init__(lengths_of_sides)

    def perimeter(self):
        '''Return the perimeter of the polygon.'''
        # calculate the perimeter
        return(self._lengths_of_sides*6)

    def area(self):
        x, y = self.lengths_of_sides
        return x * y

p = Pentagon(3)
print("Pentagon", p._lengths_of_sides)
print("The Perimeter is: ", p.perimeter())
print("Area: ", p.area())

h = Heaxagon(5)

"""
from time import time
start_time = time ()
run algorithm
end_time = time()
elapsed = end_time - start_time
"""
"""
def find_max_data:
biggest = data[0]
for val in data:
    if val > biggest:
        biggest = val
        return biggest
"""