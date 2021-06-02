# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:33:18 2020

@author: Ankit Khandewal
"""

from math import *

import matplotlib.pyplot as plt
import numpy as np


def fx(a, x):
    return x ** (a - 1) * exp(-x)


x_values = np.linspace(0, 5, 100)

y2 = []
y3 = []
y4 = []
for i in x_values:
    y2.append(fx(2, i))
    y3.append(fx(3, i))
    y4.append(fx(4, i))

plt.plot(x_values, y2)
plt.plot(x_values, y3)
plt.plot(x_values, y4)
plt.show()
