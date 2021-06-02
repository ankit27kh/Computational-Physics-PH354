"""
Home Work 5
Ankit Khandelwal
Exercise 6
15863
"""

from math import sqrt

import matplotlib.pyplot as plt
import numpy as np

M = 10.
L = 2.
vx = 0.
vy = 1.
G = 1.


def f(solution, t):
    x = solution[0]
    y = solution[1]
    r = sqrt(x ** 2 + y ** 2)
    x1 = solution[2]
    y1 = solution[3]
    fx = x1
    fy = y1
    fx1 = -G * M * x / (r ** 2 * sqrt(r ** 2 + (L ** 2) / 4))
    fy1 = -G * M * y / (r ** 2 * sqrt(r ** 2 + (L ** 2) / 4))
    return np.array([fx, fy, fx1, fy1])


ti = 0
tf = 10
N = 10000
h = (tf - ti) / N
tpoints = np.arange(ti, tf, h)
solution = np.array([1, 0, vx, vy], float)
xpoints = []
ypoints = []
x1points = []
y1points = []

for t in tpoints:
    xpoints.append(solution[0])
    ypoints.append(solution[1])
    x1points.append(solution[2])
    y1points.append(solution[3])
    k1 = h * f(solution, t)
    k2 = h * f(solution + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(solution + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(solution + k3, t + h)
    solution += (k1 + 2 * k2 + 2 * k3 + k4) / 6
plt.plot(xpoints, ypoints)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajectory')
plt.show()
