"""
Home Work 6
Ankit Khandelwal
Exercise 7
15863
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def Thomas(A, x, d):
    dd = np.copy(d)
    n = len(A)
    b = np.zeros(n + 1, float)
    c = np.zeros(n + 1, float)
    a = np.zeros(n + 1, float)
    for i in range(n):
        b[i + 1] = A[i][i]
        if i < n - 1:
            a[i + 2] = A[i + 1][i]
            c[i + 1] = A[i][i + 1]
    for i in range(1, n + 1):
        if i == 1:
            c[i] = c[i] / b[i]
            d[i - 1] = d[i - 1] / b[i]
        elif i > 1 and i < n:
            c[i] = c[i] / (b[i] - a[i] * c[i - 1])
            d[i - 1] = (d[i - 1] - a[i] * d[i - 2]) / (b[i] - a[i] * c[i - 1])
        elif i == n:
            d[i - 1] = (d[i - 1] - a[i] * d[i - 2]) / (b[i] - a[i] * c[i - 1])
    x[n - 1] = d[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = d[i - 1] - c[i] * x[i]
    return x, dd


D = 1
NN = [64, 128, 256, 512]
ans = []
count = 0
for N in NN:
    dx = 1 / N
    dt = 4 * dx ** 2 / D

    bi = 1 + 2 * D * dt / dx ** 2
    ai = -D * dt / dx ** 2
    ci = -D * dt / dx ** 2

    u = np.zeros((N, 1), float)
    v = np.zeros((N, 1), float)
    v[0][0] = 1
    v[N - 1][0] = 1
    u[0][0] = ai
    u[N - 1][0] = ci

    A = np.zeros((N, N), float)
    for i in range(N):
        if i < N - 1:
            A[i + 1][i] = ai
            A[i][i + 1] = ci
        A[i][i] = bi

    A[0][0] = bi - ai
    A[N - 1][N - 1] = bi - ci

    tv = np.linspace(0, 1, 1 / dt)
    xv = np.linspace(0, 1, N)
    f = np.zeros((N, 1), float)
    for i in range(N):
        if xv[i] > 0.4 and xv[i] < 0.6:
            f[i][0] = 1
    final = A + u @ v.T
    y = np.ones((N, 1), float)
    q = np.ones((N, 1), float)
    for t in tv:
        y, f = Thomas(A, y, f)
        q, u = Thomas(A, q, u)
        f = y - q @ ((v.T @ y) / (1 + v.T @ q))
        if count == 0 and t >= 0.025 and N == 256:
            plt.plot(xv, f, label='Time 0.025 sec, N = {}'.format(N))
            plt.legend()
            plt.xlabel('X')
            plt.ylabel('f')
            plt.figure()
            count = 1
    ans.append(f)
xpoints = []
ypoints = []
for i in range(len(NN) - 1):
    error = 0
    for j in range(NN[i]):
        error = error + float(abs(ans[i][j] - ans[i + 1][2 * j]))
    plt.scatter(1 / NN[i], error / NN[i], marker=10)
    xpoints.append(1 / NN[i])
    ypoints.append(error / NN[i])
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('dx')
    plt.ylabel('Error')
slope = linregress(xpoints, ypoints)[0]
plt.show()
