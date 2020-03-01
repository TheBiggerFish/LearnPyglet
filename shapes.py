import pyglet
from math import cos,sin,radians as rad
from pyglet.gl import GL_POLYGON, GL_TRIANGLE_STRIP, GL_LINES, glPushMatrix, glTranslatef, glRotatef, glColor3f, glPopMatrix
from point import Point2D
from copy import copy

class Shape2D:
    def __init__(self, pos, angle, drawable, color=(0,0,0), draw_method=GL_POLYGON):
        self.pos = pos #type: Point2D
        self.angle = angle #type: float
        self.color = color #type: tuple
        self.drawable = drawable #type: bool
        self.vertices = [] #type: list
        self.draw_method = draw_method #type: int

    def draw(self):
        if not self.drawable:
            raise Exception('Trying to draw non-drawable shape')
        glPushMatrix()
        glTranslatef(self.pos.x,self.pos.y,0)
        glRotatef(self.angle, 0, 0, 1)
        glColor3f(self.color[0],self.color[1],self.color[2])
        self.vlist.draw(self.draw_method)
        glPopMatrix()

    def hide(self):
        if not self.drawable:
            raise Exception('Trying to draw non-drawable shape')
        glPushMatrix()
        self.vlist = pyglet.graphics.vertex_list(0,('v2f',[]))
        glPopMatrix()

    def show(self):
        if not self.drawable:
            raise Exception('Trying to draw non-drawable shape')
        glPushMatrix()
        self.vlist = pyglet.graphics.vertex_list(len(self.vertices)//2,('v2f',self.vertices))
        glPopMatrix()


class Rectangle(Shape2D):
    def __init__(self, width, height, pos, color=(0,0,0), angle=0, drawable=True):
        super().__init__(pos,angle,drawable,color=color,draw_method=GL_TRIANGLE_STRIP)
        self.width = width
        self.height = height
        if drawable:
            x = width/2.0
            y = height/2.0
            self.vertices = [-x,-y, x,-y, -x,y, x,y]
            self.vlist = pyglet.graphics.vertex_list(4, ('v2f', self.vertices))

class Triangle(Shape2D):
    def __init__(self,pos,angle=0,color=(0,0,0),leg=120.0,inner=60.0,drawable=True):
        super().__init__(pos,angle,drawable,color=color)
        self.leg = leg
        self.inner = inner
        if drawable:
            x = cos(rad(inner/2))*leg
            y = sin(rad(inner/2))*leg
            self.vertices = [0,0,x,y,x,-y]
            self.vlist = pyglet.graphics.vertex_list(3, ('v2f',self.vertices))

class Circle(Shape2D):
    def __init__(self,pos,radius=100.0,color=(0,0,0),points=25,drawable=True):
        super().__init__(pos,0,drawable,color=color)
        self.radius = radius 
        self.points = points
        if drawable:
            for i in range(points):
                angle = rad(float(i)/points * 360)
                x = radius*cos(angle)
                y = radius*sin(angle)
                self.vertices += [x,y]
            self.vlist = pyglet.graphics.vertex_list(points, ('v2f', self.vertices))
        
class Sector(Shape2D):
    def __init__(self,pos,facing=0,inner=90.0,radius=100.0,color=(0,0,0),points=25,drawable=True):
        super().__init__(pos,facing-inner/2,drawable,color=color)
        self.radius = radius
        self.inner = inner
        self.points = points+1
        if drawable:
            self.vertices += [0,0]
            for i in range(self.points):
                curAngle = rad(float(i)/points*inner)
                x = radius*cos(curAngle)
                y = radius*sin(curAngle)
                self.vertices += [x,y]
            self.vlist = pyglet.graphics.vertex_list(len(self.vertices)//2, ('v2f', self.vertices))


class Line(Shape2D):
    def __init__(self,point1,point2,color=(0,0,0),drawable=True):
        super().__init__(Point2D(0,0),0,drawable,color,draw_method=GL_LINES)
        self.point1 = point1 #type: Point2D
        self.point2 = point2 #type: Point2D
        if drawable:
            self.vertices = [0,0, point1.x-point2.x,point1.x-point2.y]
            self.vlist = pyglet.graphics.vertex_list(2, ('v2f', self.vertices))
    def draw(self):
        self.vertices = [self.point1.x,self.point1.y, self.point2.x,self.point2.y]
        self.vlist = pyglet.graphics.vertex_list(2, ('v2f', self.vertices))
        super().draw()