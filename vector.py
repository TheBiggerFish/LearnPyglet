from point import Point2D
from math import acos,pi, hypot
class Vector2D(Point2D):
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
 
    def __mul__(self, scalar):
        return Vector2D(self.x*scalar,self.y*scalar)
    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Vector2D(self.x/scalar,self.y/scalar)

    def mag(self):
        return self.hypot()

    def norm(self):
        return self / self.mag()

    def angle(self, other):
        diff = (other - self).norm()
        if diff.y >= 0:
            return acos(diff.x)
        else:
            return 2*pi - acos(diff.x)

    #Dot product of self and other
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    #Projection of self onto other
    def proj(self, other):
        scalar = self.dot(other) / (self.mag() ** 2)
        return self * scalar

    def copy(self):
        return Vector2D(self.x,self.y)