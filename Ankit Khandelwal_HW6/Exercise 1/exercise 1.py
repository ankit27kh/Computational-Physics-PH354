"""
Home Work 6
Ankit Khandelwal
Exercise 1
15863
"""

import matplotlib.pyplot as plt
import numpy as np

mesh = 100
potential_0 = np.zeros((mesh, mesh), float)
w = 0.9
for i in range(20, 81):
    potential_0[i][20] = 1
for i in range(20, 81):
    potential_0[i][80] = -1

count = 0
while True:
    previous = np.copy(potential_0)
    for x in range(1, mesh - 1):
        for y in range(1, mesh - 1):
            if x > 19 and x < 81 and y == 20:
                potential_0[x][y] = 1
            elif x > 19 and x < 81 and y == 80:
                potential_0[x][y] = -1
            else:
                potential_0[x][y] = (1 + w) / 4 * (potential_0[x + 1][y] + potential_0[x - 1][y] \
                                                   + potential_0[x][y + 1] + potential_0[x][y - 1]) \
                                    - w * potential_0[x][y]
    if np.amax(abs(potential_0 - previous)) <= 10 ** -6:
        break
    count = count + 1
plt.imshow(potential_0, cmap='coolwarm')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.colorbar()
plt.show()
