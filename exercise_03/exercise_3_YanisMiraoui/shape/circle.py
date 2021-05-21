from numbers import Number

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
    
    def __contains__(self, other):
        centre = self.centre
        radius = self.radius
        distance = (centre[0] - other[0])**2 + (centre[1]-other[1])**2
        if distance <= radius**2: 
            return True
        else : 
            return False 
