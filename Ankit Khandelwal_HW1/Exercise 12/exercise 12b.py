'''
ANKIT KHANDELWAL
15863

Exercise 12b
'''

import math

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 10 * np.pi, 10000)
x = []
y = []
r = []
for i in theta:
    r.append(i ** 2)
for i in range(0, 10000):
    x.append(r[i] * math.cos(theta[i]))
    y.append(r[i] * math.sin(theta[i]))
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, y)
plt.show()
