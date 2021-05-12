"""
Home Work 5
Ankit Khandelwal
Exercise 5
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi

R = 0.08
rho = 1.22
C = .47
vx = 50*sqrt(3)
vy = 50
g = 9.8

def f(r, t, mass):
    x = r[0]
    y = r[1]
    x1 = r[2]
    y1 = r[3]
    fx = x1
    fy = y1
    fx1 = -pi*R**2*rho*C/2/mass * x1*sqrt(x1**2 +y1**2)
    fy1 = -g - pi*R**2*rho*C/2/mass * y1*sqrt(x1**2 + y1**2)
    return np.array([fx, fy, fx1, fy1], float)

ti = 0
tf = 20
N = 1000
h = (tf- ti)/N
tpoints = np.arange(ti, tf, h)
dis=[]

for mass in range(1, 100, 1):
    r = np.array([0, 0, vx, vy]) 
    xpoints = []
    ypoints = []
    x1points = []
    y1points = []
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        x1points.append(r[2]) 
        y1points.append(r[3])
        k1 = h*f(r, t, mass)
        k2 = h*f(r+0.5*k1, t+0.5*h, mass) 
        k3 = h*f(r+0.5*k2, t+0.5*h, mass) 
        k4 = h*f(r+k3, t+h, mass)
        r += (k1 + 2*k2 + 2*k3 + k4 )/6 
        if r[1] < 0:
            dis.append(r[0])
            break
    if mass < 10:
        plt.plot(xpoints, ypoints, label=mass)

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Trajectories')
plt.figure()
plt.plot(range(1,100,1), dis)
plt.xlabel('Mass')
plt.ylabel('Range')
plt.show()
