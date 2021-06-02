import numpy as np


def fx(x):
    return (np.sin(np.sqrt(100 * x))) ** 2


def trapezoidal(a, b, e):
    n = 1
    h = []
    er = []
    i = []
    h.append((b - a) / n)
    s = (fx(a) + fx(b)) / 2
    i.append(h[0] * s)
    er.append("   ------")
    for m in range(1, 1000, 1):
        n = 2 * n
        h.append((b - a) / n)

        i.append(0.5 * i[m - 1])
        for t in range(1, n, 2):
            i[m] = i[m] + h[m] * fx(a + (t * h[m]))
        er.append((1 / 3) * abs(i[m] - i[m - 1]))
        if er[m] <= e:
            break
    return i, er


i1, error = trapezoidal(0, 1, 1e-6)
print("n    I                       error")
for j in range(0, len(i1)):
    print(j + 1, " ", i1[j], "  ", error[j])
