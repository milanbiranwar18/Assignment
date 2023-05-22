# Design a class called "Shape" with an abstract method to calculate the area. Implement subclasses for
# specific shapes like Circle, Rectangle, and Triangle.

"""
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        radius

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        pass

    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        base
        height

    def area(self):
        pass


"""
import math
from abc import abstractmethod, ABC


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = math.pi * (self.radius**2)
        return circle_area


class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        rec_area = self.lenght * self.width
        return rec_area


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        tri_area = 1/2 * self.base * self.height
        return tri_area


if __name__ == '__main__':
    circle = Circle(5)
    print(circle.area())

    triangle = Triangle(5, 10)
    print(triangle.area())

    rect = Rectangle(10, 6)
    print(rect.area())
