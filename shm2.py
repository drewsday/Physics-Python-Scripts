from __future__ import division
from visual import *

"""
    Rodney Dunning
    Assistant Professor of Physics
    Longwood University
    
    Simple Harmonic Motion

"""

#------------------------------------------------
# dynamical variables
#------------------------------------------------

# SI units

k = 10  
A = 100
m = 1

#--------------------------------------------------
# Scene attributes and functions
#--------------------------------------------------

scene.title = "Simple Harmonic Motion"
scene.x = 0
scene.y = 0
scene.width = 600
scene.height = 600
scene.range = (1.5*A,1.5*A,1.5*A)
scene.autoscale = 0 ##0 means autoscaling is OFF
scene.userzoom = 0 ##0 means user cannot zoom
scene.userspin = 0 ##0 means user cannot spin
scene.lights = [vector(0,0,1)]
scene.ambient = 0.5
scene.label = label(visible=1,
                    pos=(0,0,0),
                    xoffset = 0,
                    yoffset = 0,
                    text = "Click to begin")
scene.mouse_label = label(visible=1,
                          pos=(0,A,0),
                          text=("Mouse position"))

def return_mouse_pos(scene):
    scene.mouse_label.text = ("mouse\n x: %3.2f   y: %3.2f"
                              %(scene.mouse.pos.x, scene.mouse.pos.y))

def check_for_pause(scene): #checks for pause request
    if scene.mouse.clicked:
        scene.mouse.getclick()
        pause(scene)

def pause(scene):
    while 1:
        return_mouse_pos(scene)
        if scene.mouse.clicked:
            scene.mouse.getclick()
            break
        
#---------------------------------------------------
# Variables for keeping up with the elapsed time.
#---------------------------------------------------

t = 0 # elapsed time
t_max = 1000 # seconds
dt = 0.01 # seconds
dt_2 = dt /2 # for the Verlet integrator in the main loop

#----------------------------------------------------
# The spring and the bob.
#----------------------------------------------------

spring = helix(pos = vector(-A,0,0),
               length = 2*A,
               coils = 25,
               radius = A/10)

spring2 = helix(pos = vector(A,0,0),
               length = 2*A,
               coils = 25,
               radius = A/10)

spring2.constant = k

spring.constant = k

bob = sphere(pos = vector(A,0,0),
             vel = vector(0,0,0),
             acc = (-1 * spring.constant / m) * vector(A,0,0),
             mass = m,
             radius = A/10)

#----------------------------------------------------
# Create reference marks--as many as needed
#----------------------------------------------------

def create_reference_marks(num_marks,range_start,step,mark_list,mark_labels):
    height = 0.1*A
    length = 0.1*height
    width = 0.1*height
    for i in range(num_marks+1):
        ref_mark = box()
        ref_mark.color = color.white
        ref_mark.height = height
        ref_mark.length = length
        ref_mark.width = width
        ref_mark.pos = vector(range_start + step*i,0,0)

        ref_mark_label = label(opacity = 0)
        ref_mark_label.pos = vector(range_start + step*i,10 + ref_mark.height/2,0)
        ref_mark_label.box = 0
        ref_mark_label.text = "%1i" %(range_start+i*step)
        
        mark_list.append(ref_mark)
        mark_labels.append(ref_mark_label)

#----------------------------------------------------
# Create bars to illustrate the energy distribution
#----------------------------------------------------

total_energy_bar = box()
total_energy_bar.color = color.red
total_energy_bar.height = 0
total_energy_bar.length = 5
total_energy_bar.width = 5
total_energy_bar.pos = (0.75*A,-0.5*A,0)

total_energy_label = label(opacity = 0)
total_energy_label.pos = vector(0.75*A,-1.1*A,0)
total_energy_label.line = 0
total_energy_label.text = "E"

potential_energy_bar = box()
potential_energy_bar.color = color.white
potential_energy_bar.height = 0
potential_energy_bar.length = 5
potential_energy_bar.width = 5
potential_energy_bar.pos = (A,-0.5*A,0)

potential_energy_label = label(opacity = 0)
potential_energy_label.pos = vector(A,-1.1*A,0)
potential_energy_label.line = 0
potential_energy_label.text = "U"

kinetic_energy_bar = box()
kinetic_energy_bar.color = color.green
kinetic_energy_bar.height = 0
kinetic_energy_bar.length = 5
kinetic_energy_bar.width = 5
kinetic_energy_bar.pos = (1.25*A,-0.5*A,0)

kinetic_energy_label = label(opacity = 0)
kinetic_energy_label.pos = vector(1.25*A,-1.1*A,0)
kinetic_energy_label.line = 0
kinetic_energy_label.text = "K"

#--------------------------------------------------------
# Main loop
#--------------------------------------------------------

ready = 0
while not ready:
    ready = scene.mouse.getclick()
    scene.label.visible = 0
    scene.label.text = "Finished."

    num_marks = int(A/10)

    reference_marks = []
    reference_labels = []

    create_reference_marks(num_marks, # number of marks
                           -A, # where the range starts
                           (2*A/num_marks), # step size
                           reference_marks,
                           reference_labels)

    E = 0.5 * k * A**2 # total energy

    potential_energy_bar.height = (0.5*k*mag(bob.pos)**2)/E
    potential_energy_bar.pos.y = -0.5*A

    total_energy_bar.height = potential_energy_bar.height + kinetic_energy_bar.height
    total_energy_bar.pos.y = -0.5*A

while t < t_max:
    rate(50)
    check_for_pause(scene)
    return_mouse_pos(scene)
    t += dt


    bob.pos += bob.vel * dt_2

    spring.length = mag(bob.pos - spring.pos)

    bob.acc = (-spring.constant / bob.mass) * bob.pos

    bob.vel += bob.acc * dt

    bob.pos += bob.vel * dt_2

    spring.length = mag(bob.pos - spring.pos)

    U_s = 0.5*k*mag(bob.pos)**2
    potential_energy_bar.height = 0.75*A*(U_s / E)
    potential_energy_bar.pos.y = -A + potential_energy_bar.height/2

    K = 0.5*bob.mass*mag(bob.vel)**2
    kinetic_energy_bar.height = 0.75*A*(K / E)
    kinetic_energy_bar.pos.y = -A + kinetic_energy_bar.height/2

    total_energy_bar.height = potential_energy_bar.height + kinetic_energy_bar.height
    total_energy_bar.pos.y = -A + total_energy_bar.height/2

scene.label.visible = 1
