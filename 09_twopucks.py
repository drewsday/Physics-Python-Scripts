from __future__ import division
from visual import *
print """
Red arrows represent force.
Click to start the motion.
Click to start over.
"""

scene.x = scene.y = 0
scene.width = 1000
scene.height = 400
scene.fov = 0.001
scene.range = 10

class disk(object):
    def __init__(self, pos=vector(0,0,0), radius=1,
                 diskcolor=color.red, stripe=color.yellow, wrap=0):
        W = 0.05*radius
        L = 2*radius
        self.pos = vector(pos)
        self.radius = radius
        self.frame = frame(pos=pos)
        cylinder(frame=self.frame, axis=(0,0,-W), radius=radius, color=diskcolor)
        box(frame=self.frame, size=(L,W,W), color=stripe)
        box(frame=self.frame, size=(W,L,W), color=stripe)
        if wrap:
            ring(frame=self.frame, pos=(0,0,-W/2), axis=(0,0,W/4),
                 radius=radius, thickness=0.7*W)
        self.frame.rotate(axis=(0,0,1), angle=0.07*pi)

xi = -8
a = 1
alpha = -0.6
dt = 0.005
yi = 2
R = 1.2
L = 1.5*R
r = 0.2*R
F = 2
rot = disk(pos=(xi,yi,0), radius=R, diskcolor=color.magenta, wrap=1)
nonrot = disk(pos=(xi,-yi,0), radius=R, diskcolor=color.green)
rot.ball = sphere(pos=rot.pos+vector(L,R,0), radius=r, color=color.yellow)
nonrot.ball = sphere(pos=nonrot.pos+vector(L,0,0), radius=r, color=color.yellow)
rot.string = curve(radius=R/40)
nonrot.string = curve(radius=R/40)
rot.force = arrow(axis=(F,0,0), color=color.red)
nonrot.force = arrow(axis=(F,0,0), color=color.red)

first = 1
while 1:
    if not first:
        scene.mouse.getclick()
    v = 0
    omega = 0
    rot.frame.pos = (xi,yi,0)
    nonrot.frame.pos = (xi,-yi,0)
    rot.string.pos = [rot.pos+vector(0,R,0),rot.pos+vector(L,R,0)]
    nonrot.string.pos = [nonrot.pos,nonrot.pos+vector(L,0,0)]
    rot.ball.pos = rot.pos+vector(L,R,0)
    nonrot.ball.pos = nonrot.pos+vector(L,0,0)
    rot.force.pos = rot.ball.pos
    nonrot.force.pos = nonrot.ball.pos
    if first:
        scene.mouse.getclick()
    first = 0

    while rot.frame.pos.x < 0:
        rate(100)
        v += a*dt
        omega += alpha*dt
        da = omega*dt
        dx = vector(v*dt,0,0)
        rot.frame.pos += dx
        nonrot.frame.pos += dx
        rot.frame.rotate(axis=(0,0,1), angle=da)
        rot.string.pos[0] += dx
        rot.string.pos[1] += dx+vector(-R*da,0,0)
        nonrot.string.pos += dx
        rot.force.pos = rot.string.pos[1]
        nonrot.force.pos += dx
        rot.ball.pos = rot.string.pos[1]
        nonrot.ball.pos += dx
