from shapes import Rectangle
from point import Point2D
from math import cos, sin
class Wall(Rectangle):
    def __init__(self,width,height,pos,angle=0,color=(0,0,0)):
        super().__init__(width,height,pos,color,angle,drawable=True)
    
    def corners(self):
        points = []
        points += [self.pos + Point2D(self.width*cos(self.angle),self.height*sin(self.angle))]
        points += [self.pos + Point2D(self.width*cos(self.angle),-self.height*sin(self.angle))]
        points += [self.pos + Point2D(-self.width*cos(self.angle),self.height*sin(self.angle))]
        points += [self.pos + Point2D(-self.width*cos(self.angle),-self.height*sin(self.angle))]
        return points

    def __straightColliding(self,other):
        if other.pos.x + other.width/2 < self.pos.x - self.width/2:
            return False
        if other.pos.y + other.height/2 < self.pos.y - self.height/2:
            return False
        if self.pos.x + self.width/2 < other.pos.x - other.width/2:
            return False
        if self.pos.y + self.height/2 < other.pos.y - other.height/2:
            return False
        return True
    
    def __simpleColliding(self,other):
        if self.width > self.height: big1 = self.width*3//2
        else: big1 = self.height*3//2
        
        if other.width > other.height: big2 = other.width/2
        else: big2 = other.height/2
        
        if not (self.pos.x + big1 > other.pos.x - big2):
            return False
        if not (self.pos.x - big1 < other.pos.x + big2):     
            return False
        if not (self.pos.y + big1 > other.pos.y - big2):
            return False
        if not (self.pos.y - big1 < other.pos.y + big2):
            return False
        return True

    def colliding(self,other):
        if not self.__simpleColliding(other):
            return False
        if self.angle == 0 and other.angle == 0:
            return self.__straightColliding(other)

        

        return True
        