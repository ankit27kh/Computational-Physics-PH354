'''
ANKIT KHANDELWAL
15863

Exercise 12a
'''

import math

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 5000)
x = []
y = []
for i in theta:
    x.append(2 * math.cos(i) + math.cos(2 * i))
    y.append(2 * math.sin(i) - math.sin(2 * i))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Deltoid Curve')
plt.plot(x, y)
plt.show()
