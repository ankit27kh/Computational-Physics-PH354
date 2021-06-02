from math import *

import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as sc


def pot(q, r):
    return q / 4 / pi / r / 100 / sc.epsilon_0


NN = 101
xv = np.linspace(-50, 50, NN)
yv = np.linspace(-50, 50, NN)

pot_grid1 = np.zeros((NN, NN))
pot_grid2 = np.zeros((NN, NN))
potgrid = np.zeros((NN, NN))
q = [-1, 1]
for z in q:
    for i in xv:
        for j in yv:
            if z == 1:
                [x1, y1] = [-5, 0]
            else:
                [x1, y1] = [5, 0]
            r = sqrt((i - x1) ** 2 + (j - y1) ** 2)
            if r == 0:
                continue
            potgrid[int(i + 50)][int(j + 50)] = pot(z, r)
    if z == 1:
        pot_grid1 = potgrid
    else:
        pot_grid2 = potgrid
    potgrid = np.zeros((NN, NN))

final_pot = pot_grid1 + pot_grid2
plt.imshow(final_pot, cmap='RdBu_r', vmin=-5 * 10 ** 5, vmax=5 * 10 ** 5)
plt.title('Potential')
plt.figure()

Ex = np.zeros((NN, NN))
Ey = np.zeros((NN, NN))

for i in xv:
    for j in yv:
        i1 = int(i + 50)
        j1 = int(j + 50)
        if j1 == 100:
            continue
        Ex[i1][j1] = (final_pot[i1][j1 + 1] - final_pot[i1][j1]) / 0.1
for j in yv:
    for i in xv:
        i1 = int(i + 50)
        j1 = int(j + 50)
        if i1 == 100:
            continue
        Ey[i1][j1] = (final_pot[i1 + 1][j1] - final_pot[i1][j1]) / 0.1

magnitude = np.sqrt(np.multiply(Ex, Ex) + np.multiply(Ey, Ey))
plt.imshow(magnitude, cmap='OrRd', vmax=5 * 10 ** 5)
plt.title('Magnitude of Electric Field')
plt.figure()

direction = np.arctan(np.divide(Ex, Ey))
plt.imshow(direction, cmap='hsv')
plt.title('Direction of Electric Field')
plt.figure()

plt.show()
