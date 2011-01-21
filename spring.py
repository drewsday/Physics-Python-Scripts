from __future__ import division
from visual import *

print"""
Spring Force:  Hooke's Law
Force = -Spring Constant * Spring Displacement
F = -kx

The program models the motion of weight attached to a spring
after the weight is pulled (stretching the spring) and released.
Friction is ignored in this model so once started the system
never stops oscillating back and forth.
"""

##########################################################################################
#
# INITIALIZE WINDOW & DECLARATIONS
#
##########################################################################################

scene.range = vector(1,1,1)
scene.center = vector(0,0,0)
scene.width = 800
scene.height = 600


##########################################################################################
#
# CREATE SPRING, WEIGHT & LABEL OBJECTS
#
##########################################################################################

relaxedlength = vector(.60,0,0) # length of spring when it isn't stretched or compressed
spring = helix(pos=(-.75,0,0),axis=relaxedlength, radius=.1,coils=8,thickness=.01,color=color.green)
spring.constant = 2 # k

weight = box(pos=(0,0,0),size=(.3,.3,.3),color=color.yellow)
weight.mass = 10 # kg
weight.velocity = vector(0,0,0)
weight.acceleration = vector(0,0,0)
weight.force = vector(0,0,0)

frictionlessSurface = box(size=(2,.02,.5),pos=(0,-.16,0))
wall = box(size=(.04,.5,.3),pos=(-.77,.1,0),color=color.red)

mylabel = label(pos=(0,.4,0))
mylabel.text = "DRAG WEIGHT TO\nSTART"                


##########################################################################################
#
# WAIT FOR USER TO DRAG THE WEIGHT
#
##########################################################################################

pick = 0
weightmoved = False
while not weightmoved:
    if scene.mouse.events:
        mouse = scene.mouse.getevent() # obtain drag or drop event
        if mouse.drag and mouse.pick == weight: # if clicked on the weight
            drag_pos = mouse.pickpos # where on the ball the mouse was
            pick = mouse.pick # pick is now the weight object (nonzero)
            scene.cursor.visible = 0 # make cursor invisible
        elif mouse.drop: # released the mouse button at end of drag
            pick = None # end dragging (None is False)
            scene.cursor.visible = 1 # cursor visible again
            weightmoved = True
    if pick:
        new_pos = scene.mouse.project(normal=(0,0,1)) # project onto xy plane
        if new_pos != drag_pos: # if the mouse has moved since last position
            pick.pos.x += new_pos.x - drag_pos.x # offset for where the weight was clicked
            # uncomment next 2 lines to limit range spring can be pulled or compressed
            #if pick.pos.x < -.35: pick.pos.x = -.35
            #if pick.pos.x > .35:  pick.pos.x = .35                
            spring.displacement = pick.pos
            spring.axis = relaxedlength + spring.displacement 
            drag_pos = new_pos # update drag position
            message = "Springs behave according to Hooke's Law only if"
            message += "\nthey aren't stretched or compressed too far."
            message += "\nTry no more than about 35 centimeters for realistic results."
            message += "\ndisplacement: %.2f meters" % spring.displacement.x 
            mylabel.text = message

##########################################################################################
#
# PULL AND RELEASE THE WEIGHT, THEN GO THRU THE LOOP
#
##########################################################################################

spring.displacement = weight.pos # the weight starts at (0,0,0) and is attached to spring
spring.axis = relaxedlength + spring.displacement

finished = False # this will always be false so it's an infinite loop
dt = .01    # seconds
seconds = 0 # total time
while not finished:
    rate(100)
