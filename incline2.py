import wx
from visual import *
display.enable_shaders = False
materials.rough = materials.diffuse

L = 20;
H = 1;
W = 3;

z0 = 1;
x0 = 1;
y0 = 1;

incline = box(pos=(x0,y0,z0), length=L, height=H, width=W)
incline.rotate(angle = pi/2.)

