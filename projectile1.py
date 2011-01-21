from visual import *

scene.width = 800
scene.height = 600

scene.autoscale = 0
scene.range = (100,100,100)
scene.center = (0,40,0)

ball = sphere(pos=(0,100,0),radius=2)
ground = box(pos=(0,-1,0),size=(10,2,10))

gravity = 9.8   # m/s**2
seconds = 0
dt = .01

finished = False           
while not finished:
    rate(100)   # go thru the loop no more than 100 times/s
    seconds += dt

    # position equation: y(t) = y0 + v0*t + .5 * a * t**2
    ballHeight = 100 - .5 * gravity * seconds**2

    ball.pos = vector(0,ballHeight,0)

    if ballHeight - 2 < 0:
        finished = True
        print "seconds to fall: " + str(seconds)
