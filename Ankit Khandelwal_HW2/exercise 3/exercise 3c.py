import numpy as np


def f(x):
    return (np.sin(np.sqrt(100 * x))) ** 2


def adaptive_simpson(a, b, e):
    n = 2
    h = []
    er = []
    S = []
    T = []
    i = []
    h.append((b - a) / n)
    s = (f(a) + f(b)) * (1 / 3)
    t = (2 / 3) * f(a + h[0])
    S.append(s)
    T.append(t)
    i.append(h[0] * (S[0] + (2 * T[0])))
    er.append("   ------------")
    for m in range(1, 1000, 1):
        sum2 = 0
        n = 2 * n
        h.append((b - a) / n)
        S.append(S[m - 1] + T[m - 1])
        for k in range(1, n, 2):
            sum2 = sum2 + f(a + (k * h[m]))
        T.append((2 / 3) * sum2)
        i.append(h[m] * (S[m] + (2 * T[m])))
        er.append((1 / 15) * abs(i[m] - i[m - 1]))
        if er[m] <= e:
            break
    return i, er


i1, error = adaptive_simpson(0, 1, 1e-6)
p = 1
print("n    I                           error")
for j in range(0, len(i1)):
    p = 2 * p
    print(p, " ", i1[j], "  ", error[j])
