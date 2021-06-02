'''
Ankit Khandelwal
15863
Home Work 7
Exercise 8a
'''

from math import sin, cos, pi, log, sqrt, exp

import matplotlib.pyplot as plt

a = 2227057010910366687
M = 2 ** 64 - 59
x1 = 12375675  # seed
x2 = 35436811  # seed
x3 = 36876145  # seed

kb = 1
Tmax = 2
Tmin = 10 ** -6
tau = 10 ** 4

N = int(tau * log(Tmax / Tmin) + 1)

sigma = 1
delta = []
for i in range(int(N / 2) + 1):
    x1 = int(a * x1) % M
    theta = 2 * pi * x1 / (M - 1)
    x2 = int(a * x2) % M
    z = x2 / (M - 1)
    r = sqrt(-2 * sigma * log(z))
    delta.append(r * cos(theta))
    delta.append(r * sin(theta))


def f(x):
    return x ** 2 - cos(4 * pi * x)


x = 2
E = f(x)
xx = [2]
for i in range(N):
    T = Tmax * exp(-i / tau)
    beta = 1 / kb / T
    x = x + delta[i]
    E_new = f(x)
    delta_E = E_new - E
    x3 = int(a * x3) % M
    y3 = (x3 / (M - 1))
    if y3 > exp(-beta * delta_E):
        x = x - delta[i]
        E = E
    else:
        E = E_new
    xx.append(x)
print('Minimum is at x = {}'.format(x))
plt.plot(xx, '.', markersize=1)
plt.ylabel('x')
plt.xlabel('Steps')
plt.show()
