import math


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        result = Circle.pi * math.pow(self.radius, 2)
        return float(str(round(result, 2)))

    def get_circumference(self):
        result = 2 * Circle.pi * self.radius
        return result

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
