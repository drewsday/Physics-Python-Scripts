# written by Lenore Horner, 2009

from visual import *

Ndrops = 10
toggle = 0  # 0 makes all drops the same mass; 1 makes all drops the same density
power = 2
constant = .5
dropheight = 4
dt = 0.01

floor = box(length=8, height=0.5, width=8, pos=(0,-dropheight,0), color=color.blue)
Drops = []

for i in range(Ndrops):        # create drops of various sizes at rest at common height
	size = random.uniform(0.1,1)
	Drops = Drops + [ellipsoid(length = size, width = size, height = size, color=color.red)]
	Drops[i].velocity = vector(0,0,0)
	Drops[i].acceleration = vector(0,9.8,0)
	Drops[i].pos = vector(random.uniform(-3.5,3.5),dropheight,random.uniform(-3.5,3.5))

#scene.mouse.getclick()          # hold the drops until we're ready to drop them
	
while 1:
    rate(100)
    for i in range(Ndrops):                                 # let all the drops fall
		Drops[i].pos = Drops[i].pos + Drops[i].velocity*dt
		if Drops[i].y < -dropheight + Drops[i].height + 0.5:        # check for drops hitting surface
			if Drops[i].height > 0.09:                     # only worry about drops that haven't already gone splat
				Drops[i].velocity.y = 0                   # drops stop
				# drops flatten on surface
				Drops[i].height = 0.09
				Drops[i].length = Drops[i].width = Drops[i].width**(3.0/2)
				Drops[i].pos.y = -dropheight + 0.5					
		else:
		    Drops[i].velocity.y = Drops[i].velocity.y + Drops[i].acceleration.y*dt
		    volume = Drops[i].width**2 * Drops[i].height
		    accel = sign(Drops[i].velocity.y) * constant*Drops[i].width**2*Drops[i].velocity.y**power / (volume)**toggle
		    Drops[i].acceleration.y = -9.8 - accel