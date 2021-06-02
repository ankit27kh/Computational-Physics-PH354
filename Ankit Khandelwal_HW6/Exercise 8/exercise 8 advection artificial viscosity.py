"""
Home Work 6
Ankit Khandelwal
Exercise 8
15863
"""

from math import exp

import matplotlib.pyplot as plt
import numpy as np

v = 1


def sqr(x):
    if x >= 0.6 and x <= 0.8:
        return 1
    else:
        return 0


def u0(x):
    return exp(-200 * (x - 0.3) ** 2) + sqr(x)


N = 128
dx = 1 / N
dt = 0.5 * dx / v
dis = 2
xv = np.linspace(0, dis, dis * N)
tv = np.linspace(0, 3, int(1 / dt))
qcon = 25
l = qcon * dx
nsub = 2 * qcon * 10
tvis = dt / 2 / qcon
tsub = dt / nsub

u = np.zeros(dis * N)
for i in range(N):
    u[i] = u0(xv[i])
u_new = np.copy(u)
u_new_new = np.copy(u)

for t in tv:
    if t in [0, 1, 2, 3]:
        plt.plot(xv, u_new, label=t)
        plt.legend()
        plt.title('Lax-Wendroff')
    for i in range(dis * N - 1):
        u_half1 = 1 / 2 * (u[i + 1] + u[i]) - dt / 2 / dx * ((u[i + 1]) - (u[i]))
        u_half2 = 1 / 2 * (u[i] + u[i - 1]) - dt / 2 / dx * ((u[i]) - (u[i - 1]))
        u_new[i] = u[i] - dt / dx * ((u_half1) - (u_half2))

    q = np.zeros(dis * N, float)
    for x in range(dis * N - 1):
        if (u_new[x + 1] - u_new[x]) / dx < 0:
            q[x] = l ** 2 * ((u_new[x + 1] - u_new[x]) / dx) ** 2
        else:
            q[x] = 0

    for t1 in range(int(nsub)):
        for x in range(dis * N - 1):
            u_new_new[x] = u_new[x] - tsub * (q[x + 1] - q[x]) / dx
    u = np.copy(u_new_new)
plt.show()
