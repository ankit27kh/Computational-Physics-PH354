"""
Home Work 5
Ankit Khandelwal
Exercise 8b
15863
"""

from math import sqrt
from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np

start = perf_counter()

M = 1.989 * 10 ** 30
vx = 0
vy = 15768000
G = 6.6375 * 10 ** -5
x0 = 4 * 10 ** 9
y0 = 0


def f(solution, t):
    x = solution[0]
    y = solution[1]
    r = sqrt(x ** 2 + y ** 2)
    x1 = solution[2]
    y1 = solution[3]
    fx = x1
    fy = y1
    fx1 = -G * M * x / r ** 3
    fy1 = -G * M * y / r ** 3
    return np.array([fx, fy, fx1, fy1])


ti = 0
tf = 2 * 48
h = .0005
tpoints = np.arange(ti, tf, h)
solution = np.array([x0, y0, vx, vy], float)
xpoints = []
ypoints = []

for t in tpoints:
    xpoints.append(solution[0])
    ypoints.append(solution[1])
    k1 = h * f(solution, t)
    k2 = h * f(solution + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(solution + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(solution + k3, t + h)
    solution += (k1 + 2 * k2 + 2 * k3 + k4) / 6
plt.plot(xpoints, ypoints)
plt.xlabel('X in km')
plt.ylabel('Y in km')
plt.title('Trajectory')
plt.show()

end = perf_counter()
print('Time taken = {} seconds for 1 orbit.'.format((end - start) / 2))
