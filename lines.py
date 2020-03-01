import pyglet
from pyglet.gl import glClearColor, glClear, GL_COLOR_BUFFER_BIT
from point import Point2D
from shapes import Line

window = pyglet.window.Window(width=1000,height=700,resizable=True)

ticks = 120

cur = Line(Point2D(0,0),Point2D(0,0),drawable=True)
lines = []
started = False

@window.event
def on_draw():
    global started
    glClearColor(1, 0.9, 0.8, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    if not started:
        return
    cur.draw()
    for line in lines:
        line.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    global started
    started = True
    cur.point1 = Point2D(x,y)
    cur.point2 = Point2D(x,y)
    pass

@window.event
def on_mouse_release(x, y, button, modifiers):
    global lines
    cur.point2 = Point2D(x,y)
    lines += [Line(cur.point1.copy(),cur.point2.copy())]
    pass

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    cur.point2 = Point2D(x,y)
    pass

def update(dummy):
    pass

pyglet.clock.schedule_interval(update,1/ticks)
pyglet.app.run()