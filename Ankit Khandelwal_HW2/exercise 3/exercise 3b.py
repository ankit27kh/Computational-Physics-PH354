import numpy as np


def fx(x):
    return (np.sin(np.sqrt(100 * x))) ** 2


def romberg(a, b, e):
    R = np.zeros([20, 20], float)
    n = 1
    p = 0
    s = (fx(a) + fx(b)) / 2
    R[1, 1] = s
    R[1, 0] = 1
    error = 2 * e
    i = 2
    while error > e:
        p = 0 + i
        R[i, 0] = p
        n = 2 * n
        h = ((b - a) / n)

        R[i, 1] = 0.5 * R[i - 1, 1]
        for t in range(1, n, 2):
            R[i, 1] = R[i, 1] + h * fx(a + (t * h))
        for m in range(1, i, 1):
            epsilon = (1 / ((4 ** m) - 1)) * (R[i, m] - R[(i - 1), m])
            R[i, (m + 1)] = R[i, m] + epsilon
            error = abs(epsilon)
        i = i + 1

    return R, p


r, n = romberg(0, 1, 1e-6)
for k in range(1, n + 1, 1):
    print(r[k, 0:(k + 1)])
