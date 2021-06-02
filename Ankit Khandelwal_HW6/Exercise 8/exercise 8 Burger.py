"""
Home Work 6
Ankit Khandelwal
Exercise 8 Burger
15863
"""

from math import sin, pi

import matplotlib.pyplot as plt
import numpy as np

N = 128
xi = 0
xf = 1
xv = np.linspace(xi, xf, N)
dx = (xf - xi) / N
dt = 0.5 * dx
tv = np.linspace(0, 0.5, int(1 / dt))


def u0(x):
    return sin(2 * pi * x)


def f(u):
    return u ** 2 / 2


u = np.zeros(N, float)
for i in range(N):
    u[i] = u0(xv[i])
u_new = np.copy(u)
count = 0
for t in tv:
    if t >= 0 and count == 0:
        plt.plot(xv, u_new, label=t)
        count = 1
    elif t >= 0.1 and count == 1:
        plt.plot(xv, u_new, label=t)
        count = 2
    elif t >= 0.25 and count == 2:
        plt.plot(xv, u_new, label='0.25')
        count = 3
    elif t >= 0.5 and count == 3:
        plt.plot(xv, u_new, label=t)
        count = 4
    for i in range(N):
        if i < N - 1:
            u_new[i] = (u[i + 1] + u[i - 1]) / 2 - dt / 2 / dx * (f(u[i + 1]) - f(u[i - 1]))
        else:
            u_new[i] = (u[0] + u[i - 1]) / 2 - dt / 2 / dx * (f(u[0]) - f(u[i - 1]))
    u = np.copy(u_new)

plt.legend()
plt.xlabel('X')
plt.ylabel('u')
plt.title('Lax')

u = np.zeros(N, float)
for i in range(N):
    u[i] = u0(xv[i])
u_new = np.copy(u)
count = 0
plt.figure()
for t in tv:
    if t >= 0 and count == 0:
        plt.plot(xv, u_new, label='0')
        count = 1
    elif t >= 0.1 and count == 1:
        plt.plot(xv, u_new, label='0.1')
        count = 2
    elif t >= 0.25 and count == 2:
        plt.plot(xv, u_new, label='0.25')
        count = 3
    elif t >= 0.5 and count == 3:
        plt.plot(xv, u_new, label='0.5')
        count = 4
    for i in range(N):
        if u[i] >= 0:
            u_new[i] = u[i] + dt / dx * (f(u[i - 1]) - f(u[i]))
        elif i < N - 1 and u[i] <= 0:
            u_new[i] = u[i] + dt / dx * (f(u[i]) - f(u[i + 1]))
        else:
            u_new[i] = u[i] + dt / dx * (f(u[i]) - f(u[0]))
    u = np.copy(u_new)
plt.legend()
plt.xlabel('X')
plt.ylabel('u')
plt.title('Upwinding')

u = np.zeros(N, float)
for i in range(N):
    u[i] = u0(xv[i])
u_new = np.copy(u)
count = 0
plt.figure()
for t in tv:
    if t >= 0 and count == 0:
        plt.plot(xv, u_new, label='0')
        count = 1
    elif t >= 0.1 and count == 1:
        plt.plot(xv, u_new, label='0.1')
        count = 2
    elif t >= 0.25 and count == 2:
        plt.plot(xv, u_new, label='0.25')
        count = 3
    elif t >= 0.5 and count == 3:
        plt.plot(xv, u_new, label='0.5')
        count = 4
    for i in range(N):
        if i < N - 1:
            u_half1 = 1 / 2 * (u[i + 1] + u[i]) - dt / 2 / dx * (f(u[i + 1]) - f(u[i]))
            u_half2 = 1 / 2 * (u[i] + u[i - 1]) - dt / 2 / dx * (f(u[i]) - f(u[i - 1]))
            u_new[i] = u[i] - dt / dx * (f(u_half1) - f(u_half2))
        else:
            u_half1 = 1 / 2 * (u[0] + u[i]) - dt / 2 / dx * (f(u[0]) - f(u[i]))
            u_half2 = 1 / 2 * (u[i] + u[i - 1]) - dt / 2 / dx * (f(u[i]) - f(u[i - 1]))
            u_new[i] = u[i] - dt / dx * (f(u_half1) - f(u_half2))
    u = np.copy(u_new)

plt.legend()
plt.xlabel('X')
plt.ylabel('u')
plt.title('Lax-Wendroff')
plt.show()
