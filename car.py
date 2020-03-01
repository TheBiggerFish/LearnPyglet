import sys
from shapes import Rectangle,Sector
from math import sin, cos, radians as rad, degrees as deg, pi, sqrt
from point import Point2D
from vector import Vector2D

class Car:
    def __init__(self,pos=Point2D(0,0),angle=0,velocity=0,maxVelocity=5,bodyWidth=30,bodyLength=60,headlightsOn=False,headlightPower=100):
        self.pos = pos #type: Point
        self.velocity = velocity #type: float
        self.maxVelocity = maxVelocity
        self.angle = angle #type: float

        self.headlightsOn = headlightsOn #type: bool
        self.headlightPower = headlightPower #type: int
        self.height = bodyWidth #type: int
        self.width = bodyLength #type: int
        
        self.__body = Rectangle(bodyLength,bodyWidth,pos,color=(1,0,0))
        self.__headlight1 = Sector(Point2D(pos.x,pos.y),angle,inner=40,color=(1,1,0.5))
        self.__headlight1.hide()
        self.__headlight2 = Sector(Point2D(pos.x,pos.y),angle,inner=40,color=(1,1,0.5))
        self.__headlight2.hide()

    def velocityVector(self):
        x = cos(rad(self.angle))*self.velocity
        y = sin(rad(self.angle))*self.velocity
        return Vector2D(x,y)

    def draw(self):
        if self.headlightsOn:
            self.__headlight1.draw()
            self.__headlight2.draw()
        self.__body.draw()
    
    def turnBy(self,angle,mustMove=True):
        newAngle = self.angle
        if(mustMove):
            newAngle += angle * (self.velocity / self.maxVelocity)
        else:
            newAngle += angle
        if newAngle >= 360:
            newAngle -= 360
        elif newAngle < 0:
            newAngle += 360
        self.face(newAngle)

    def turnToward(self,point,gradual=True):
        if self.pos.dist(point) < 0.1:
            return
        posdiff = point - self.pos
        angle = Vector2D(posdiff.x,posdiff.y)
        angle = deg(Vector2D(1,0).angle(angle))
        diff = angle - self.__body.angle
        if diff > 180:
            diff -= 360
        elif diff <= -180:
            diff += 360

        if abs(diff) < 0.01:
            diff = 0
            return

        if gradual and diff > 0:
            diff = sqrt(diff/100)
        elif gradual and diff < 0:
            diff = -sqrt(-diff/100)

        if diff != 0:
            self.turnBy(diff,mustMove=False)

    def face(self,angle):
        self.angle = angle
        self.__body.angle = self.angle
        self.__headlight1.angle = self.__body.angle - self.__headlight1.inner/2
        self.__headlight2.angle = self.__body.angle - self.__headlight2.inner/2

    def accelerate(self,deltaV):
        self.velocity += deltaV
        if self.velocity > self.maxVelocity:
            self.velocity = self.maxVelocity
        elif self.velocity < -self.maxVelocity:
            self.velocity = -self.maxVelocity

    def brake(self,deltaV):
        if self.velocity > 0:
            self.velocity -= deltaV
        if self.velocity < 0:
            self.velocity += deltaV
        if abs(self.velocity) < 0.0000001:
            self.velocity = 0

    #Implementation of Craig Reynold's Boids Arrival Simulation
    #https://slsdo.github.io/steering-behaviors/
    def arrival(self,pos,radius):
        e = pos - self.pos
        dist = e.hypot()
        if dist < 0.01:
            dist = 0
        if dist > 0 and dist < radius:
            self.velocity = self.maxVelocity * (dist/radius)
        elif dist > radius:
            self.velocity = self.maxVelocity

    def drive(self):
        self.pos += self.velocityVector()

        if self.headlightsOn:
            self.__headlight1.pos.x = self.pos.x + cos(rad(self.angle+20))*30
            self.__headlight1.pos.y = self.pos.y + sin(rad(self.angle+20))*30

            self.__headlight2.pos.x = self.pos.x + cos(rad(self.angle-20))*30
            self.__headlight2.pos.y = self.pos.y + sin(rad(self.angle-20))*30
        self.__body.pos = self.pos

    def toggleHeadlights(self):
        self.headlightsOn = not self.headlightsOn
        if not self.headlightsOn:
            self.__headlight1.hide()
            self.__headlight2.hide()
        else:
            self.__headlight1.show()
            self.__headlight2.show()

    def isMoving(self):
        return self.velocity != 0


    @property
    def body(self):
        return self.__body
    @property
    def headlight1(self):
        return self.__headlight1
    @property
    def headlight2(self):
        return self.__headlight2

    @property
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self,pos):
        self.__pos = pos

    @property
    def maxVelocity(self):
        return self.__maxVelocity
    @maxVelocity.setter
    def maxVelocity(self,maxVelocity):
        self.__maxVelocity = maxVelocity

    @property
    def velocity(self):
        return self.__velocity
    @velocity.setter
    def velocity(self,velocity):
        self.__velocity = velocity

    @property
    def angle(self):
        return self.__angle
    @angle.setter
    def angle(self,angle):
        self.__angle = angle

    @property
    def headlightsOn(self):
        return self.__headlightsOn
    @headlightsOn.setter
    def headlightsOn(self,headlightsOn):
        self.__headlightsOn = headlightsOn

    @property
    def headlightPower(self):
        return self.__headlightPower
    @headlightPower.setter
    def headlightPower(self,headlightPower):
        self.__headlightPower = headlightPower
