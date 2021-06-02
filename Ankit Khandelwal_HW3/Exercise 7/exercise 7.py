"""
Ankit Khandelwal
15863
Exercise 7
"""

from math import sqrt, tan, pi

from scipy.constants import c

m = 0.511 * 10 ** 6 / c ** 2
L = 10 ** -9
V = 20
hbar = 6.582 * 10 ** -16
u02 = m * (L ** 2) * V / 2 / hbar ** 2


def fe1(v):
    return sqrt(u02 - v ** 2)


def fe2(v):
    return v * tan(v)


def cot(x):
    return 1 / tan(x)


def fo1(v):
    return sqrt(u02 - v ** 2)


def fo2(v):
    return -v * cot(v)


def fe(v):
    return fe1(v) - fe2(v)


v_val = []
Energy_e = []
for i in range(3):
    a = i * pi + 0.2
    b = (2 * i + 1) * pi / 2 - 0.1
    x = (a * fe(b) - b * fe(a)) / (fe(b) - fe(a))
    while abs(fe(x)) > 10 ** -4 and (b - a) > 10 ** -10:
        if fe(a) * fe(x) < 0:
            a = a
            b = x
        elif fe(a) * fe(x) > 0:
            a = x
            b = b
        x = (a * fe(b) - b * fe(a)) / (fe(b) - fe(a))
    v_val.append(x)
    Energy_e.append(((2 * hbar * v_val[i] / L) ** 2) / 2 / m)
print(Energy_e, 'For even solution')


def fo(v):
    return fo1(v) - fo2(v)


v_val = []
Energy_o = []
for i in range(3):
    a = (2 * i + 1) * pi / 2 + 0.2
    b = (i + 1) * pi - 0.1
    x = (a * fo(b) - b * fo(a)) / (fo(b) - fo(a))
    while abs(fo(x)) > 10 ** -4 and (b - a) > 10 ** -10:
        if fo(a) * fo(x) < 0:
            a = a
            b = x
        elif fo(a) * fo(x) > 0:
            a = x
            b = b
        x = (a * fo(b) - b * fo(a)) / (fo(b) - fo(a))
    v_val.append(x)
    Energy_o.append(((2 * hbar * v_val[i] / L) ** 2) / 2 / m)
print(Energy_o, 'For odd solution')

print('First 6 Energy states are:')
T_E = Energy_e + Energy_o
T_E.sort()
print(T_E)
