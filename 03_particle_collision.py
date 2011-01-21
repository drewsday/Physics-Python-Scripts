from __future__ import division
from visual import *
print """
Bruce Sherwood Fall 2000
modified S2006 to show p's, allow mouse input to pause (Ruth Chabay)

Collision between particles whose parameters can be varied.
Change "b" (impact parameter) to see what happens.
Note 90 degrees between outgoing momenta.
Comment in two lines just before while loop to change to
center of momentum frame, where the collision looks much simpler.
"""   

## impact parameter
##b = 0
b = 15e-15  
##b = 80e-15

projectileproperties = (2,4) # alpha particle charge/e, mass/mp
##projectileproperties = (-1,(9e-31/1.7e-27))    ## electron

targetproperties = (8,16) # oxygen nucleus charge/3, mass/mp
##targetproperties = (2,4) # alpha particle
##targetproperties = (1,(9e-31/1.7e-27))    ## positron

rpscale = 2 ## make radii bigger for visual impact
parroVisible = 1

scene.width = 1000
scene.height = 750
scene.x = scene.y = 0
scene.background = color.white
scene.fov = 0.01
scene.range = 200e-15
xstart = scene.range.x*0.95

kcoul = 9e9
qe = 1.6e-19
mproton = 1.7e-27
rproton = 1.3e-15*rpscale
alpha = sphere(pos=(-xstart,b,0), color=color.red)
target = sphere(pos=(0,0,0), color=color.blue)
alpha.mass = projectileproperties[1]*mproton
alpha.radius = (alpha.mass/mproton)**(1./3.)*rproton
alpha.q = projectileproperties[0]*qe
ke = 1e6*qe
alpha.p = vector(sqrt(2.*alpha.mass*ke),0,0)
alpha.trail = curve(color=alpha.color)
target.mass = targetproperties[1]*mproton
target.radius = (target.mass/mproton)**(1./3.)*rproton
target.q = targetproperties[0]*qe
target.p = vector(0,0,0)
target.trail = curve(color=target.color)
dt = (5.*xstart/(mag(alpha.p)/alpha.mass)/1e5)*1
ptot = alpha.p+target.p
vcm = ptot/(alpha.mass+target.mass)

pscale = 40e-15/4e-20
paarro = arrow(pos=alpha.pos, axis=alpha.p*pscale, color=color.cyan,
               shaftwidth = 0.5*alpha.radius, fixedwidth=1, visible=parroVisible)
ptarro = arrow(pos=target.pos, axis=target.p*pscale, color=color.magenta,
               shaftwidth = 0.5*alpha.radius, fixedwidth=1, visible=parroVisible)
print alpha.p
print target.p

# Comment in these statements to view in center of mass frame
##alpha.p = alpha.p-alpha.mass*vcm
##target.p = target.p-target.mass*vcm

##scene.autoscale = 0
scene.mouse.getclick()  ## click to start particle moving
while True:
    r12 = alpha.pos-target.pos
    F = (kcoul*alpha.q*target.q/mag(r12)**2)*norm(r12)
    alpha.p = alpha.p + F*dt
    target.p = target.p - F*dt
    alpha.pos = alpha.pos + (alpha.p/alpha.mass)*dt
    target.pos = target.pos + (target.p/target.mass)*dt
    paarro.pos = alpha.pos
    paarro.axis = alpha.p*pscale
    ptarro.pos = target.pos
    ptarro.axis = target.p*pscale
    alpha.trail.append(pos=alpha.pos)
    target.trail.append(pos=target.pos)
    if scene.mouse.clicked:
        scene.mouse.getclick()  ## take original click
        scene.mouse.getclick()  ## pause and wait for new click




