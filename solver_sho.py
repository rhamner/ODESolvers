def diffEQ(t, x, v):
	return float(v), float(-x)


import matplotlib.pyplot as plt

#Euler
currentx = 1;
currentv = 0;
currentt = 0;
dt = .001;
xa, va, ta = [], [], []

while currentt <= 400:
	currentt = currentt + dt
	x, v = diffEQ(currentt, currentx, currentv)
	currentv = currentv + dt*v
	currentx = currentx + dt*x
	ta.append(currentt)
	xa.append(currentx)
	va.append(currentv)

plt.figure(1)
plt.plot(ta, xa)
plt.ylabel('x')
plt.xlabel('t')
plt.title('Euler')
plt.figure(2)
plt.plot(xa, va)
plt.ylabel('v')
plt.xlabel('x')
plt.title('Euler')

#Runge-Kutta 4
currentx = 1;
currentv = 0;
currentt = 0;
dt = .01;
xa, va, ta = [], [], []

while currentt <= 400:
	k1x, k1v = diffEQ(currentt, currentx, currentv)
	k1x = dt*k1x
	k1v = dt*k1v
	k2x, k2v = diffEQ(currentt + dt/2, currentx + k1x/2, currentv + k1v/2)
	k2x = dt*k2x
	k2v = dt*k2v
	k3x, k3v = diffEQ(currentt + dt/2, currentx + k2x/2, currentv + k2v/2)
	k3x = dt*k3x
	k3v = dt*k3v
	k4x, k4v = diffEQ(currentt + dt, currentx + k3x, currentv + k3v)
	k4x = dt*k4x
	k4v = dt*k4v
	
	currentx = currentx + (k1x + 2*k2x + 2*k3x + k4x)/6
	currentv = currentv + (k1v + 2*k2v + 2*k3v + k4v)/6
	currentt = currentt + dt
	
	ta.append(currentt)
	xa.append(currentx)
	va.append(currentv)

plt.figure(3)
plt.plot(ta, xa)
plt.ylabel('x')
plt.xlabel('t')
plt.title('Runge-Kutta')
plt.figure(4)
plt.plot(xa, va)
plt.ylabel('v')
plt.xlabel('x')
plt.title('Runge-Kutta')
plt.show()





