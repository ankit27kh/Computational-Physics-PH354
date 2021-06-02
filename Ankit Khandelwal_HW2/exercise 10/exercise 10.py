import math as math
from cmath import *

import numpy as np


def der(m):
    mf = math.factorial(m)
    N = 10000
    j = sqrt(-1)

    def fz(z):
        return exp(2 * z)

    k = np.linspace(0, N, N + 1)
    Z = []
    for i in k:
        Z.append(exp(j * 2 * pi * i / N))
    I = 0
    for i in k:
        if i == N:
            continue
        I = I + fz(Z[int(i)]) * exp(-j * 2 * pi * m * i / N)
    return mf / N * I


for i in range(1, 21):
    print(der(i).real)
