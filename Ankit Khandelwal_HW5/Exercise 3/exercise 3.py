"""
Home Work 5
Ankit Khandelwal
Exercise 3
15863
"""

import matplotlib.pyplot as plt
import numpy as np

sigma = 10.
r = 28.
b = 8 / 3


def f(solution, t):
    x = solution[0]
    y = solution[1]
    z = solution[2]
    fx = sigma * (y - x)
    fy = r * x - y - x * z
    fz = x * y - b * z
    return np.array([fx, fy, fz])


ti = 0
tf = 50
N = 100000
h = (tf - ti) / N
tpoints = np.arange(ti, tf, h)
xpoints = []
ypoints = []
zpoints = []
solution = np.array([0, 1, 0], float)
for t in tpoints:
    xpoints.append(solution[0])
    ypoints.append(solution[1])
    zpoints.append(solution[2])
    k1 = h * f(solution, t)
    k2 = h * f(solution + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(solution + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(solution + k3, t + h)
    solution += (k1 + 2 * k2 + 2 * k3 + k4) / 6

plt.plot(tpoints, ypoints)
plt.xlabel('Time')
plt.ylabel('Y')
plt.figure()
plt.plot(xpoints, zpoints)
plt.xlabel('X')
plt.ylabel('Z')
plt.show()
