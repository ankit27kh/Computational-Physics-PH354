'''
Ankit Khandelwal
15863
Home Work 7
Exercise 11b
'''

from math import ceil, pi, sin, cos, sqrt

import matplotlib.pyplot as plt
import numpy as np

a = 2227057010910366687
M = 2 ** 64 - 59

L = 100  # Edge = 2*L + 1
r = 0

A = 1
B = 5

x1 = 1913557377  # seed
x_s1 = 233252557  # seed

data_x = [0]
data_y = [0]
grid = np.zeros((2 * L + 1, 2 * L + 1), int)
grid[L][L] = 1
stuck = 1
final = 0
while final < 1:
    x_s1 = int(a * x_s1) % M
    y1 = x_s1 / (M - 1)
    z_s1 = ((2 * pi) * y1)
    x_start = ceil((r + 1) * cos(z_s1))
    y_start = ceil((r + 1) * sin(z_s1))
    count = 0
    xpos = [x_start]
    ypos = [y_start]
    while True:
        x1 = int(a * x1) % M
        y1 = x1 / (M - 1)
        z1 = int(A + (B - A) * y1)
        if z1 == 1:
            ypos.append(ypos[-1] + 1)
            xpos.append(xpos[-1])
        if z1 == 3:
            xpos.append(xpos[-1])
            ypos.append(ypos[-1] - 1)
        if z1 == 2:
            xpos.append(xpos[-1] + 1)
            ypos.append(ypos[-1])
        if z1 == 4:
            ypos.append(ypos[-1])
            xpos.append(xpos[-1] - 1)

        r_new = sqrt(xpos[-1] ** 2 + ypos[-1] ** 2)
        if r_new > 2 * sqrt(x_start ** 2 + y_start ** 2) or r_new > L / 2:
            break

        if grid[-ypos[-1] + L][xpos[-1] + L] == 1:
            grid[-ypos[-2] + L][xpos[-2] + L] = 1
            count = 1

        if count == 1:
            data_x.append(xpos[-2])
            data_y.append(ypos[-2])
            stuck = stuck + 1
            r_new = sqrt(xpos[-2] ** 2 + ypos[-2] ** 2)
            if r_new > r:
                r = r_new
            if r > L / 2:
                final = 1
            break

A = plt.scatter(data_x, data_y, marker='.', s=2, c=range(stuck), cmap='cool')
plt.title('Edge length {}'.format(2 * L + 1))
plt.xlim(-L, L)
plt.ylim(-L, L)
A.axes.set_facecolor('black')
A.axes.get_xaxis().set_ticks([])
A.axes.get_yaxis().set_ticks([])
plt.show()
