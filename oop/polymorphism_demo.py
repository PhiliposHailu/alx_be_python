import math

class Shape:
    
    def area(self):
        raise(NotImplementedError)

class Rectangle(Shape):

    def __init__(self, radius, width) -> None:
        self.radius = radius
        self.width = width

    def area(self):
        return self.radius * self.width
    
class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
        


