import pyglet
from pyglet.gl import glClearColor, glClear, GL_COLOR_BUFFER_BIT
from car import Car
from point import Point2D

window = pyglet.window.Window(width=1000,height=700,resizable=True)

ticks = 120
car = Car(pos=Point2D(window.get_size()[0]//2,window.get_size()[1]//2),velocity=3,maxVelocity=3)

@window.event
def on_mouse_motion(x, y, dx, dy):
    global mousePos
    mousePos = Point2D(x,y)
        

@window.event
def on_draw():
    glClearColor(0, 0.1, 0.2, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    car.draw()

def update(dummy):
    global mousePos, oldPos
    if not (oldPos.x == mousePos.x and oldPos.y == mousePos.y):
        oldPos.x = mousePos.x
        oldPos.y = mousePos.y
    car.turnToward(mousePos)
    car.arrival(mousePos,250)
    car.drive()

mousePos = Point2D(0,0)
oldPos = Point2D(0,0)


pyglet.clock.schedule_interval(update,1/ticks)
pyglet.app.run()