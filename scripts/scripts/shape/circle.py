from shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, diameter):
        self.diameter = diameter
        

    def area(self):
        return round(pi * ((self.diameter/2)**2))
    
x = Circle(10)
print(x.area())

