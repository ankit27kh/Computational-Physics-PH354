'''
Ankit Khandelwal
15863
Home Work 7
Exercise 9
'''

from math import exp, log

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

a = 2227057010910366687
M = 2 ** 64 - 59

L = 50
grid = np.zeros((L + 2, L + 2), int)
grid[0, :] = -1
grid[L + 1, :] = -1
grid[:, 0] = -1
grid[:, L + 1] = -1

x = 24613417  # seed
x1 = 541362405  # seed
x2 = 3761273  # seed

covering = []
for i in range(L + 2):
    covering.append(i)
    if i == 0 or i == L + 1:
        for j in range(1, L + 2, 1):
            covering.append(j * (L + 2) + i)
    else:
        covering.append(i + (L + 1) * (L + 2))
grid_new = np.copy(grid)
n = 0
dimers = (np.count_nonzero(grid) - len(covering)) / 2
energy = -dimers
kb = 1
Tmax = 1
Tmin = 10 ** -6
tau = 10 ** 4

N = int(tau * log(Tmax / Tmin) + 1)
steps = np.ndarray(N, np.ndarray)
dimer_step = []

fig = plt.figure()
ax = plt.axes()
cmap = plt.cm.Spectral_r
cmap.set_bad(color='black')
A = plt.imshow(grid_new[1:L + 1, 1:L + 1], cmap=cmap, animated=True)
A.axes.get_xaxis().set_ticks([])
A.axes.get_yaxis().set_ticks([])

for i in range(N):
    T = Tmax * exp(-i / tau)
    beta = 1 / kb / T
    site1 = 0
    while site1 in covering:
        x = int(a * x) % M
        site1 = int(x / (M - 1) * (L + 2) ** 2)
    site2 = 0
    while site2 in covering:
        x1 = int(a * x1) % M
        y1 = int(4 * x1 / (M - 1))
        if y1 == 0: site2 = site1 - 1
        if y1 == 1: site2 = site1 + (L + 2)
        if y1 == 2: site2 = site1 + 1
        if y1 == 3: site2 = site1 - (L + 2)
    i1 = site1 // (L + 2)
    i2 = site2 // (L + 2)
    j1 = site1 % (L + 2)
    j2 = site2 % (L + 2)
    if grid[i1][j1] == 0 and grid[i2][j2] == 0:
        n = n + 1
        grid_new[i1][j1] = n
        grid_new[i2][j2] = n
    elif grid[i1][j1] == grid[i2][j2] and grid[i1][j1] != 0:
        grid_new[i1][j1] = 0
        grid_new[i2][j2] = 0
    dimers = (np.count_nonzero(grid_new) - len(covering)) / 2
    energy_new = -dimers
    delta_E = energy_new - energy
    x2 = int(a * x2) % M
    y2 = x2 / (M - 1)
    if y2 > exp(-beta * delta_E):
        energy = energy
        grid_new = np.copy(grid)
    else:
        energy = energy_new
        grid = np.copy(grid_new)
    steps[i] = grid[1:L + 1, 1:L + 1]
    dimer_step.append(dimers)


def animate(i):
    steps[i] = np.ma.masked_where(steps[i] < 0.1, steps[i])
    A.set_array(steps[i])
    norm = plt.Normalize(np.min(steps[i]), np.max(steps[i]))
    A.set_norm(norm)
    ax.set_title('Step = {} with Dimers ={}'.format(i, int(dimer_step[i])))


anim = animation.FuncAnimation(fig, animate, frames=N, interval=10)
# anim.save('e9.mp4')
