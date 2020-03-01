import pyglet
from car import Car
from point import Point2D
from wall import Wall
from random import randint

window = pyglet.window.Window(width=1000,height=700,resizable=True)
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

ticks = 120
car = Car(pos=Point2D(500,500),maxVelocity=1)
walls = []

@window.event
def on_draw():
    pyglet.gl.glClearColor(0.8, 0.9, 1, 0)
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    for wall in walls:
        wall.draw()
    car.draw()

fpressed = False
def update(dummy):
    global ticks
    global fpressed
    global walls
    
    acc = 0
    if keyboard[pyglet.window.key.UP] or keyboard[pyglet.window.key.W]:
        car.accelerate(30/ticks)
    if keyboard[pyglet.window.key.DOWN] or keyboard[pyglet.window.key.S]:
        car.accelerate(-30/ticks)
    if keyboard[pyglet.window.key.SPACE]:
        car.brake(30/ticks)

    if car.isMoving():
        if keyboard[pyglet.window.key.LEFT] or keyboard[pyglet.window.key.A]:
            car.turnBy(1.5)
        if keyboard[pyglet.window.key.RIGHT] or keyboard[pyglet.window.key.D]:
            car.turnBy(-1.5)
    if keyboard[pyglet.window.key.F] and not fpressed:
        fpressed = True
        car.toggleHeadlights()
    elif not keyboard[pyglet.window.key.F] and fpressed:
        fpressed = False

    colliding = False
    for wall in walls:
        if wall.colliding(car):
            car.velocity = 0.5
            colliding = True
    if not colliding:
        car.velocity = 2
    
    
    car.drive()

def generateWalls():
    global walls
    for i in range (10):
        wall = Wall(0,0,Point2D(0,0))
        colliding = True
        while(colliding):
            width = randint(5,10) * 10
            height = randint(5,10) * 10
            pos = Point2D.randPoint((width,1000-width/2),(height,700-height/2))
            wall = Wall(width,height,pos)
            colliding = False
            for other in walls:
                if(wall.colliding(other)):
                    colliding = True
                    break
        walls += [wall]
    pass

generateWalls()
pyglet.clock.schedule_interval(update,1/ticks)
pyglet.app.run()