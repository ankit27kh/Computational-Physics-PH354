"""
Home Work 6
Ankit Khandelwal
Exercise 7
15863
"""

from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve_banded
from scipy.stats import linregress

D = 1
NN = [64, 128, 256, 512, 1024]
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
    v[N - 1][0] = -ai / bi
    u[0][0] = -bi
    u[N - 1][0] = ci

    A_banded = np.zeros((3, N), float)
    A_banded[0, 1:] = ci
    A_banded[1, :] = bi
    A_banded[2, :N - 1] = ai

    A_banded[1][0] = 2 * bi
    A_banded[1][N - 1] = ai * ci / bi + bi

    tv = np.linspace(0, 1, 1 / dt)
    xv = np.linspace(0, 1, N)
    f = np.zeros((N, 1), float)
    for i in range(N):
        if xv[i] > 0.4 and xv[i] < 0.6:
            f[i][0] = 1
    y = np.ones((N, 1), float)
    q = np.ones((N, 1), float)
    t1 = perf_counter()
    for t in tv:
        y = solve_banded((1, 1), A_banded, f, overwrite_b=True, check_finite=False)
        q = solve_banded((1, 1), A_banded, u, overwrite_b=False, check_finite=False)
        f = y - q @ ((v.T @ y) / (1 + v.T @ q))
        if count == 0 and t >= 0.025 and N == 256:
            plt.plot(xv, f, label='Time 0.025 sec, N = {}'.format(N))
            plt.legend()
            plt.xlabel('X')
            plt.ylabel('f')
            plt.figure()
            count = 1
    ans.append(f)
    t2 = perf_counter()
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
