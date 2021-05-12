"""
Home Work 5
Ankit Khandelwal
Exercise 10
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

G = 6.6738*10**-11
M = 1.9891*10**30
m = 5.9722*10**24

def f(posr, velr, t):
    x = posr[0]
    y = posr[1]
    x1 = velr[0]
    y1 = velr[1]
    fx = x1
    fy = y1
    R = sqrt(x**2 + y**2)
    fx1 = -G*M*x/R**3
    fy1 = -G*M*y/R**3
    position = [fx, fy]
    velocity = np.array([fx1, fy1])
    return velocity

h = 3600.
ti = 0.
tv = np.arange(ti, 10*365*24*60*60, h)

posr = np.array([1.4710*10**11, 0])
velr = np.array([0, 3.0287*10**4])

xv = []
yv = []
x1v = []
y1v = []
x11 = [0]
y11 = [3.0287*10**4]
v_step = np.array([x11, y11])
v = (v_step[0]**2 + v_step[1]**2)
KE = [.5*m*v]
radius = sqrt(posr[0]**2+posr[1]**2)
PE = [-G*M*m/radius]

for t in tv:
    xv.append([posr[0]])
    yv.append([posr[1]])
    x1v.append([velr[0]])
    y1v.append([velr[1]])
    velr = velr + 0.5*h*f(posr, velr, t)
    if t == ti:
        x1v[0] = [velr[0]]
        y1v[0] = [velr[1]]
    posr = posr + h*velr
    k = h*f(posr, velr, t+h)
    x11.append(v_step[0])
    y11.append(v_step[1])
    v_step = velr + k/2
    velr = velr + k
    v = (v_step[0]**2 + v_step[1]**2)
    KE.append(1/2*m*v)
    radius = sqrt(posr[0]**2+posr[1]**2)
    PE.append(-G*M*m/radius)
        
plt.plot(xv, yv)
plt.xlabel('X')
plt.ylabel('Y')
plt.figure()
plt.plot(tv, KE[:-1], label='Kinetic Energy')
plt.plot(tv, PE[:-1], label='Potential Energy')
plt.plot(tv, np.add(KE[:-1],PE[:-1]), label='Total Energy')
plt.legend(loc='upper right', fancybox=True, framealpha=0.5)
plt.xlabel('Time')
plt.ylabel('Energy')
plt.figure()
plt.plot(tv, np.add(KE[:-1],PE[:-1]), label='Total Energy')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Energy')
plt.show()
