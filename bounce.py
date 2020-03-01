import pyglet
from pyglet.gl import glClearColor,glClear,GL_COLOR_BUFFER_BIT
from ball import Ball
from point import Point2D
from vector import Vector2D
from random import randint, random,uniform

width, height = 1000,700
window = pyglet.window.Window(width=width,height=height,resizable=True)
ticks = 120
balls = []

@window.event
def on_draw():
    global width, height
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    for ball in balls:
        ball.draw()

def generate():
    global width,height
    global balls
    for num in range(5):
        ball = Ball(Point2D(0,0),0,Vector2D(0,0),(1,1,1))
        colliding = True
        while(colliding):
            radius = randint(1,10) * 10
            pos = Point2D.randPoint((radius,width-radius),(radius,height-radius))
            vel = Vector2D(uniform(-3,3),uniform(-3,3))
            ball = Ball(pos,radius,vel,(random(),random(),random()))

            colliding = False
            for other in balls:
                if(ball.colliding(other)):
                    colliding = True
                    break
        balls += [ball]

#https://gamedevelopment.tutsplus.com/tutorials/when-worlds-collide-simulating-circle-circle-collisions--gamedev-769
def update(dummy):
    for ball1 in balls:
        ball1.tryUpdate()
        for ball2 in balls:
            if ball1 != ball2:
                ball1.collide(ball2)
        ball1.bounce(Point2D(window.get_size()[0],window.get_size()[1]))

generate()
pyglet.clock.schedule_interval(update,1/ticks)
pyglet.app.run()