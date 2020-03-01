from shapes import Circle
from point import Point2D
from math import pi
from vector import Vector2D

class Ball(Circle):
    def __init__(self,pos,radius,vel,color):
        super().__init__(pos,radius,color)
        self.vel = vel #type: Vector2D
        self.__collided = False
    
    def update(self):
        self.pos += self.vel

    def tryUpdate(self):
        if not self.__collided:
            self.update()
        self.__collided = False

    def speed(self):
        return self.vel.mag()

    def mass(self):
        return pi * (self.radius**2)

    def dist(self, other):
        return self.pos.dist(other.pos)

    #Surface distance
    def surfDist(self,other):
        return self.dist(other) - (self.radius + other.radius)

    def simpleColliding(self,other):
        if not (self.pos.x + self.radius > other.pos.x - other.radius):
            return False
        if not (self.pos.x - self.radius < other.pos.x + other.radius):
            return False
        if not (self.pos.y + self.radius > other.pos.y - other.radius):
            return False
        if not (self.pos.y - self.radius < other.pos.y + other.radius):
            return False
        return True

    def colliding(self, other):
        if not self.simpleColliding(other):
            return False
        return self.surfDist(other) <= 0

    def bounce(self,corner):
        if self.pos.x - self.radius <= 0 and self.vel.x < 0:
            self.vel.x = -self.vel.x
        if self.pos.x + self.radius >= corner.x and self.vel.x > 0:
            self.vel.x = -self.vel.x
        if self.pos.y - self.radius <= 0 and self.vel.y < 0:
            self.vel.y = -self.vel.y
        if self.pos.y + self.radius >= corner.y and self.vel.y > 0:
            self.vel.y = -self.vel.y

    def collide(self, other):
        if not self.colliding(other):
            return

        v1mass = 2 * other.mass() / (self.mass() + other.mass())
        v1posd = Vector2D(self.pos.x - other.pos.x, self.pos.y - other.pos.y)
        v1dot = (self.vel - other.vel).dot(v1posd)
        v1mag = (v1posd).mag() ** 2

        v2mass = 2 * self.mass() / (self.mass() + other.mass())
        v2posd = Vector2D(other.pos.x - self.pos.x,other.pos.y-self.pos.y)
        v2dot = (other.vel - self.vel).dot(v2posd)
        v2mag = (v2posd).mag() ** 2

        self.vel = self.vel - v1mass * v1dot * v1posd / v1mag
        self.update()
        self.__collided = True
        other.vel = other.vel - v2mass * v2dot * v2posd / v2mag
        other.update()
        other.__collided = True