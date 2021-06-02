"""
Home Work 5
Ankit Khandelwal
Exercise 4d
15863
"""

import matplotlib.pyplot as plt
import numpy as np

w = 1


def f(r, t):
    x = r[0]
    y = r[1]
    fx = y
    fy = -w ** 2 * x ** 3
    return np.array([fx, fy])


ti = 0
tf = 50
N = 1000
h = (tf - ti) / N
tpoints = np.arange(ti, tf, h)

x1 = [.5, 1., 2.]
for i in x1:
    r = np.array([i, 0.])
    xpoints = []
    ypoints = []
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h * f(r, t)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(r + k3, t + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    plt.figure(1)
    plt.plot(tpoints, xpoints, label=i)
    plt.figure(2)
    plt.plot(xpoints, ypoints, label=i)
plt.figure(1)
plt.xlabel('Time')
plt.ylabel('X')
plt.legend()
plt.figure(2)
plt.xlabel('X')
plt.ylabel('dx/dt')
plt.title('Phase Space')
plt.legend()
plt.show()
