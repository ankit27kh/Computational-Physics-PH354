"""
Home Work 5
Ankit Khandelwal
Exercise 14
15863
"""

import matplotlib.pyplot as plt
import numpy as np


def f(r, t):
    u = r[0]
    v = r[1]
    fu = 998 * u + 1998 * v
    fv = -999 * u - 1999 * v
    return np.array([fu, fv])


t_stable = 2 / 1999

h = [t_stable / 2, 10 * t_stable]

ti = 0
tf = 10

for i in range(2):
    tv = np.arange(ti, tf, h[i])
    upoints = []
    vpoints = []
    r = np.array([1, 0], float)
    for t in tv:
        upoints.append(r[0])
        vpoints.append(r[1])
        r = r + h[i] * f(r, t)
    plt.figure(i)
    plt.plot(tv, upoints, label='u')
    plt.plot(tv, vpoints, label='v')
    plt.title(h[i])
    plt.legend()

for i in range(2):
    tv = np.arange(ti, tf, h[i])
    upoints = []
    vpoints = []
    r = np.array([1, 0], float)
    upoints.append(r[0])
    vpoints.append(r[1])
    for t in tv:
        r = r + h[i] * f(r, t)
        upoints.append(r[0])
        vpoints.append(r[1])
        r = r - np.linalg.inv(np.array(([998, 1998], [-999, -1999]))) @ f(r, t)
    plt.figure(i + 2)
    plt.plot(tv, upoints[:-1], label='u')
    plt.plot(tv, vpoints[:-1], label='v')
    plt.title(h[i])
    plt.legend()
plt.show()
