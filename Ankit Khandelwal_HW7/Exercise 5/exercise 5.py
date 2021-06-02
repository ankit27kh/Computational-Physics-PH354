'''
Ankit Khandelwal
15863
Home Work 7
Exercise 5
'''

from math import pi

import numpy as np
from numpy.linalg import norm

a = 2227057010910366687
M = 2 ** 64 - 59

N = 1000000
d = 10
x = np.zeros((N + 1, d))
y = np.zeros((N + 1, d))
z = np.zeros((N, d))

A = -1
B = 1

x[0, :] = np.arange(7143545, 2 * d + 7143545, 2)  # seed

for i in range(1, N + 1, 1):
    for j in range(d):
        x[i][j] = (int(a * x[i - 1][j])) % M
        y[i][j] = x[i][j] / (M - 1)
        z[i - 1][j] = A + (B - A) * y[i][j]

k = np.zeros(N)
for i in range(N):
    if norm(z[i, :]) ** 2 <= 1:
        k[i] = 1

I = 2 ** d / N * sum(k)
print('Calculated volume = {}, theoretical volume = {}'.format(I, pi ** 5 / 120))
