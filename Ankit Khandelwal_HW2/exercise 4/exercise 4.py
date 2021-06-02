from math import *

import scipy.constants as sc


def simpsons_rule(f, a, b):
    c = (a + b) / 2.0
    h3 = abs(b - a) / 6.0
    return h3 * (f(a) + 4.0 * f(c) + f(b))


def recursive_asr(f, a, b, eps, whole):
    c = (a + b) / 2.0
    left = simpsons_rule(f, a, c)
    right = simpsons_rule(f, c, b)
    if abs(left + right - whole) <= 15 * eps:
        return left + right + (left + right - whole) / 15.0
    return recursive_asr(f, a, c, eps / 2.0, left) + recursive_asr(f, c, b, eps / 2.0, right)


def adaptive_simpsons_rule(f, a, b, eps):
    return recursive_asr(f, a, b, eps, simpsons_rule(f, a, b))


def f(x):
    return x ** 3 / (exp(x) - 1)


Ans = adaptive_simpsons_rule(f, 0 + 10 ** -10, 100, 10 ** -10)

stefan = Ans * sc.Boltzmann ** 4 / 4 / pi ** 2 / sc.speed_of_light ** 2 / sc.hbar ** 3
print(stefan, 'value from program')
print(sc.Stefan_Boltzmann, 'Actural value')
