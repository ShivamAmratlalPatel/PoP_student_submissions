from numbers import Number
from math import sqrt

class Circle:
    def __init__(self, centre: tuple, radius: Number):
        self.centre = centre
        self.radius = radius
    
    def __contains__(self, point: tuple):
        if sqrt((point[0] - self.centre[0])**2 + (point[1] - self.centre[1])**2) <= self.radius:
            return True
        else:
            return False