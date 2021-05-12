"""
Home Work 5
Ankit Khandelwal
Exercise 2
15863
"""

import numpy as np
import matplotlib.pyplot as plt

alpha = 1.
beta = .5
gamma = .5
delta = 2.

def f(r, t):
    x = r[0]
    y = r[1]
    fx = alpha*x - beta*x*y
    fy = gamma*x*y - delta*y    
    return np.array([fx, fy])

ti = 0
tf = 30
N = 10000
h = (tf- ti)/N
tpoints = np.arange(ti, tf, h)
xpoints = []
ypoints = []
r = np.array([2.0 ,2.0]) 
for t in tpoints:
    xpoints.append(r[0]) 
    ypoints.append(r[1]) 
    k1 = h*f(r, t)
    k2 = h*f(r+0.5*k1, t+0.5*h) 
    k3 = h*f(r+0.5*k2, t+0.5*h) 
    k4 = h*f(r+k3, t+h)
    r += (k1 + 2*k2 + 2*k3 + k4 )/6 

plt.plot(tpoints, xpoints, label='Rabbit population')
plt.plot(tpoints, ypoints, label='Fox population')
plt.xlabel('Time')
plt.ylabel('X 1000 population')
plt.legend()
plt.show()
