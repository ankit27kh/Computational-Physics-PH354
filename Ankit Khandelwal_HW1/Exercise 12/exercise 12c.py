'''
ANKIT KHANDELWAL
15863

Exercise 12c
'''

from math import *

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 24 * np.pi, 50000)
x = []
y = []
r = []
for i in theta:
    r.append(exp(cos(i)) - 2 * cos(4 * i) + sin(i / 12) ** 5)
for i in range(0, 50000):
    x.append(r[i] * cos(theta[i]))
    y.append(r[i] * sin(theta[i]))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fey\'s Function')
plt.plot(x, y)
plt.show()
