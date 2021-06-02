'''
Ankit Khandelwal
15863
Home Work 7
Exercise 11
'''

import matplotlib.pyplot as plt
import numpy as np

a = 2227057010910366687
M = 2 ** 64 - 59
c = 0

L = 100  # Edge = 2*L + 1
grid = np.zeros((2 * L + 3, 2 * L + 3), int)

A = 1
B = 5
x1 = 556817437  # seed

data_x = []
data_y = []
stuck = 0
final = 0

while final < 1:
    count = 0
    xpos = [0]
    ypos = [0]
    while True:
        if grid[L + 1][L + 1] == 1:
            count = 1

        if count == 0:
            x1 = int(a * x1 + c) % M
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
            if xpos[-1] > L:
                xpos[-1] = L
                grid[-ypos[-1] + L + 1][xpos[-1] + L + 1] = 1
                count = 1
            if ypos[-1] > L:
                ypos[-1] = L
                grid[-ypos[-1] + L + 1][xpos[-1] + L + 1] = 1
                count = 1
            if xpos[-1] < -L:
                xpos[-1] = -L
                grid[-ypos[-1] + L + 1][xpos[-1] + L + 1] = 1
                count = 1
            if ypos[-1] < -L:
                ypos[-1] = -L
                grid[-ypos[-1] + L + 1][xpos[-1] + L + 1] = 1
                count = 1
            if grid[-ypos[-1] + L + 1][xpos[-1] + L + 1] == 1:
                grid[-ypos[-2] + L + 1][xpos[-2] + L + 1] = 1
                count = 1
        if count == 1:
            if xpos[-1] == 0 and ypos[-1] == 0:
                final = 1
                break
            data_x.append(xpos[-2])
            data_y.append(ypos[-2])
            stuck = stuck + 1
            break

A = plt.scatter(data_x, data_y, marker='.', s=2, c=range(stuck), cmap='cool')
plt.title('Edge length {}'.format(2 * L + 1))
plt.xlim(-L, L)
plt.ylim(-L, L)
A.axes.set_facecolor('black')
A.axes.get_xaxis().set_ticks([])
A.axes.get_yaxis().set_ticks([])
plt.show()
