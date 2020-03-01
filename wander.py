import pyglet
from pyglet.gl import *
from car import Car
from point import Point2D
from random import randrange,random
from math import pi, cos, sin

window = pyglet.window.Window(width=1000,height=700,resizable=True)

ticks = 120
car = Car(pos=Point2D(window.get_size()[0]//2,window.get_size()[1]//2),velocity=1,maxVelocity=1)

@window.event
def on_draw():
    glClearColor(0, 0.1, 0.2, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    car.draw()

point = Point2D(randrange(window.get_size()[0]),window.get_size()[1])
def update(dummy):
    global point
    if point.dist(car.pos) < 300:
        x = randrange(window.get_size()[0])
        y = randrange(window.get_size()[1])
        newPoint = Point2D(x,y)
        while newPoint.dist(point) > 300:
            x = randrange(window.get_size()[0])
            y = randrange(window.get_size()[1])
            newPoint = Point2D(x,y)
        point = newPoint
    car.turnToward(point)
    car.drive()

pyglet.clock.schedule_interval(update,1/ticks)
pyglet.app.run()