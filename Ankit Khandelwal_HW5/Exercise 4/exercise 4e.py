"""
Home Work 5
Ankit Khandelwal
Exercise 4e
15863
"""

import numpy as np
import matplotlib.pyplot as plt

w = 1

def f(r, t, mu):
    x = r[0]
    y = r[1]
    fx = y
    fy = mu*(1-x**2)*y - w**2*x
    return np.array([fx, fy])

ti = 0
tf = 20
N = 1000
h = (tf- ti)/N
tpoints = np.arange(ti, tf, h)


for mu in [1,2,4]:
    r = np.array([1., 0.]) 
    xpoints = []
    ypoints = []
    for t in tpoints:
        xpoints.append(r[0]) 
        ypoints.append(r[1]) 
        k1 = h*f(r, t, mu)
        k2 = h*f(r+0.5*k1, t+0.5*h, mu) 
        k3 = h*f(r+0.5*k2, t+0.5*h, mu) 
        k4 = h*f(r+k3, t+h, mu)
        r += (k1 + 2*k2 + 2*k3 + k4 )/6 
    plt.plot(xpoints, ypoints, label=mu)

plt.xlabel('X')
plt.ylabel('dx/dt')
plt.title('Phase Space')
plt.legend()
plt.show()
