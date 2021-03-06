from visual import *

theta=pi/20.;

L = 20;
H = 1;
W = 3;

z0 = 1;
x0 = 1;
y0 = 1;

X0 = (L-1)*cos(theta);
Y0 = (L)*sin(theta)+W/2.;

g = 9.8;
m = 1;
t = 0

ay = m*g*sin(theta)*sin(theta)
ax = m*g*sin(theta)*cos(theta)

dt = 0.01


incline = box(pos=(L/2.*cos(theta),L/2.*sin(theta),0), length=L, height=H, width=W)
incline.rotate(angle=theta, axis =(0,0,1))

cart = box(pos=((L-1)*cos(theta),(L)*sin(theta)+W/2.,0), length = 4, height = 2, width=3,color=(0,1,1))
cart.rotate(angle=theta, axis=(0,0,1))

cart.pos.X0 == cart.pos.x;
cart.pos.Y0 == cart.pos.y;

while cart.pos.x > 0:
	rate(100)
	t = t + dt;
	print cart.pos.x
	cart.pos.x = cart.pos.X0 - .5*ax*t**2
	cart.pos.y = cart.pos.Y0 - .5*ay*t**2
#	cart(pos=((L-1)*cos(theta)-.5*ax*t**2,(L)*sin(theta)+W/2.-.5*ay*t**2,0))



