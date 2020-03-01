import pyglet
from car import Car
from point import Point2D

window = pyglet.window.Window(width=1000,height=700,resizable=True)
keyboard = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboard)

ticks = 120
car = Car(pos=Point2D(500,500),maxVelocity=5)

@window.event
def on_draw():
    pyglet.gl.glClearColor(0, 0.1, 0.2, 0)
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    car.draw()
    
fpressed = False
def update(dummy):
    global ticks
    global fpressed
    
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
    car.drive()
 
pyglet.clock.schedule_interval(update,1/ticks)
pyglet.app.run()