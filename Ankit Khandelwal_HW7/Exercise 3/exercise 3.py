'''
Ankit Khandelwal
15863
Home Work 7
Exercise 3
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

a = 2227057010910366687
M = 2 ** 64 - 59
c = 0

N = 1000000

x1 = np.zeros(N + 1)
y1 = np.zeros(N + 1)
z1 = np.zeros(N, int)

xpos = np.zeros(N + 1, int)
ypos = np.zeros(N + 1, int)
L = 50  # Edge = 2*L+1

A = 1
B = 5
col = np.zeros(N)
x1[0] = 3968251  # seed

for i in range(1, N + 1, 1):
    col[i - 1] = (i)
    x1[i] = int(a * x1[i - 1] + c) % M
    y1[i] = x1[i] / (M - 1)
    z1[i - 1] = A + (B - A) * y1[i]
    if z1[i - 1] == 1:
        ypos[i] = ypos[i - 1] + 1
        xpos[i] = xpos[i - 1]
    if z1[i - 1] == 3:
        xpos[i] = xpos[i - 1]
        ypos[i] = ypos[i - 1] - 1
    if z1[i - 1] == 2:
        xpos[i] = xpos[i - 1] + 1
        ypos[i] = ypos[i - 1]
    if z1[i - 1] == 4:
        ypos[i] = ypos[i - 1]
        xpos[i] = xpos[i - 1] - 1
    if xpos[i] > L:
        xpos[i] = L
        i = i - 1
    if ypos[i] > L:
        ypos[i] = L
        i = i - 1
    if xpos[i] < -L:
        xpos[i] = -L
        i = i - 1
    if ypos[i] < -L:
        ypos[i] = -L
        i = i - 1

A, ax = plt.subplots()
points = np.array([xpos, ypos]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
norm = plt.Normalize(col.min(), col.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(col)
lc.set_linewidth(1)
line = ax.add_collection(lc)
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
A.colorbar(line, ax=ax)
A = plt.scatter(0, 0, s=100, marker='*', c='k', label='Start')
A = plt.scatter(xpos[-1], ypos[-1], s=10, marker='s', c='k', label='End')
plt.legend(loc='upper right')
plt.show()
