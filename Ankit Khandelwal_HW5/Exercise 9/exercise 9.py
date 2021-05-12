"""
Home Work 5
Ankit Khandelwal
Exercise 9
15863
"""

import numpy as np
import matplotlib.pyplot as plt
 
def f(r, t):
    x = r[0]
    y = r[1]
    fx = y
    fy = y**2 - x - 5    
    return np.array([fx, fy])

ti = 0
tf = 50
h = 0.001
xpoints = []
ypoints = []
r = np.array([1.0 ,0.0])

tv = np.arange(ti+h, tf-h, h)
xv = [r[0]]
yv = [r[1]]

r0_5 = r + 0.5*h*f(r, ti)
r = r +h*f(r0_5, ti+h/2)

for t in tv:
    xv.append(r[0]) 
    yv.append(r[1])
    r0_5 = r0_5 + h*f(r, t)
    r = r + h*f(r0_5, t)

tv = np.arange(ti, tf-h, h)

plt.plot(tv, xv)
plt.xlabel('Time')
plt.ylabel('X')
plt.show()
