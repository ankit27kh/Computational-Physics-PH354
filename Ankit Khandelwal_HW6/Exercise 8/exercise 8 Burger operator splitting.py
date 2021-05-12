"""
Home Work 6
Ankit Khandelwal
Exercise 8 Burger
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi

N = 128
xi = 0
xf = 1
xv = np.linspace(xi, xf, N)
dx = (xf-xi)/N
dt = 0.5*dx
tv = np.linspace(0, 1, int(1/dt))
qcon = 1.6
l = qcon * dx
nsub = 2*qcon*10
tvis = dt/2/qcon
tsub = dt/nsub

def u0(x):
    return sin(2*pi*x)

def f(u):
    return u**2/2

u = np.zeros(N, float)
for i in range(N):
    u[i] = u0(xv[i])
u_new = np.copy(u)
u_new_new = np.copy(u)
count = 0
for t in tv:
    
    if t >= 0 and count == 0:
        plt.plot(xv, u, label='0')
        count = 1
    elif t >= 0.1 and count == 1:
        plt.plot(xv, u, label='0.1')
        count = 2
    elif t >= 0.25 and count == 2:
        plt.plot(xv, u, label='0.25')
        count = 3
    elif t >= 0.5 and count == 3:
        plt.plot(xv, u, label='0.5')
        count = 4
    
    for i in range(N-1):
            u_half1 = 1/2*(u[i+1] + u[i]) - dt/2/dx * (f(u[i+1]) - f(u[i]))
            u_half2 = 1/2*(u[i] + u[i-1]) - dt/2/dx * (f(u[i]) - f(u[i-1]))
            u_new[i] = u[i] - dt/dx * (f(u_half1) - f(u_half2))

    q = np.zeros(N, float)
    for x in range(N-1):
            if (u_new[x+1]-u_new[x])/dx < 0:
                q[x] = l**2 * ((u_new[x+1]-u_new[x])/dx)**2
            else:
                q[x] = 0
    
    for t1 in range(int(nsub)):
        for x in range(N-1):
            u_new_new[x] = u_new[x]  - tsub * (q[x+1] - q[x])/dx
    u = np.copy(u_new_new)

plt.legend()
plt.xlabel('X')
plt.ylabel('u')
plt.title('Lax-Wendroff')
plt.show()
