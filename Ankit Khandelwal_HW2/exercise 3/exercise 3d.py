import numpy as np


def f(x):
    return (np.sin(np.sqrt(100 * x))) ** 2


def romberg(a, b, e):
    R = np.zeros([20, 20], float)
    n = 2
    p = 0
    h = ((b - a) / n)
    s = (f(a) + f(b)) * (1 / 3)
    t = (2 / 3) * f(a + h)
    R[1, 1] = h * (s + 2 * t)
    R[1, 0] = 1
    error = 2 * e
    i = 2
    while error > e:
        p = 0 + i
        R[i, 0] = p
        sum2 = 0
        n = 2 * n
        h = ((b - a) / n)
        s = s + t
        for k in range(1, n, 2):
            sum2 = sum2 + f(a + (k * h))
        t = (2 / 3) * sum2
        R[i, 1] = (h * (s + (2 * t)))
        for m in range(1, i, 1):
            epsilon = (1 / ((4 ** m) - 1)) * (R[i, m] - R[(i - 1), m])
            R[i, (m + 1)] = R[i, m] + epsilon
            error = abs(epsilon)
        i = i + 1

    return R, p


r, n = romberg(0, 1, 1e-6)
for k in range(1, n + 1, 1):
    print(r[k, 0:(k + 1)])
