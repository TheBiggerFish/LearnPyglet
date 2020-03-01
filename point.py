from math import sqrt, acos, pi, hypot, degrees
from random import randrange

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x #type: float
        self.y = y #type: float
    
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
 
    def __mul__(self, scalar):
        return Point2D(self.x*scalar,self.y*scalar)
    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return Point2D(self.x/scalar,self.y/scalar)

    def hypot(self):
        return hypot(self.x,self.y)

    def dist(self, other):
        return (self - other).hypot()
    
    def copy(self):
        return Point2D(self.x,self.y)

    @staticmethod
    def randPoint(x,y):
        rx = randrange(x[0],x[1])
        ry = randrange(y[0],y[1])
        return Point2D(rx,ry)


    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        self.__y = y