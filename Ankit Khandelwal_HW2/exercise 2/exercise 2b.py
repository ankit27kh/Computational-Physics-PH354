from math import *

import matplotlib.pyplot as plt
import numpy as np


def simpson(n, fx, a, b):
    h = (b - a) / n
    x_values = np.linspace(a, b, n + 1)
    I = 0
    for i in range(0, n - 1, 2):
        j = x_values[i]
        S = h / 3 * (fx(j) + 4 * fx(j + h) + fx(j + 2 * h))
        I = I + S
    return I


def J(m, x):
    def fx(th):
        return cos(m * th - x * sin(th))

    return 1 / pi * (simpson(1000, fx, 0, pi))


lamda = 500 * 10 ** -9
k = 2 * pi / lamda


def I(r):
    if r == 0:
        return 1 / 4
    else:
        return (J(1, k * r) / k / r) ** 2


NN = 100
yv = np.linspace(-10 ** -6, 10 ** -6, NN)
xv = np.linspace(-10 ** -6, 10 ** -6, NN)
final = np.ones((NN, NN))

for x in range(NN):
    for y in range(NN):
        r = sqrt(xv[x] ** 2 + yv[y] ** 2)
        final[x][y] = I(r)
plt.imshow(final, cmap='gray', vmax=0.005)
plt.title('Diffraction Pattern')
plt.show()
