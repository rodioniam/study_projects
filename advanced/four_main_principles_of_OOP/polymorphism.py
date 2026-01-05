import math


# in parent class i define function, but do nnit give it any logic
class Shape:
    def calc_area(self):
        pass


# but depending on subclass this function will do different things
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * pow(self.radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(4, 10), Circle(7), Rectangle(25, 15)]

result = [shape.calc_area() for shape in shapes]

print(result)
