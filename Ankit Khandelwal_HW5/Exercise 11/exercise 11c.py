"""
Home Work 5
Ankit Khandelwal
Exercise 11c
15863
"""

from math import sqrt

import matplotlib.pyplot as plt
import numpy as np

energy_trial = [[200, 300], [300, 800], [800, 1500]]
energy = np.zeros((3))
N = 2000
wavefunction = np.zeros((3, N + 1))


def slv(E):
    psi = 0.01
    phi = 0.0
    r = ([psi, phi])
    N = 2000
    L = 10
    x_points = np.linspace(-L, L, N + 1)
    wavefunc = np.zeros((1, N + 1))
    h = (2 * L) / N
    for k in range(N):
        wavefunc[0][k] = r[0]
        x = x_points[k]
        k1 = h * f(r, x, E)
        k2 = h * f(r + 0.5 * k1, x + 0.5 * h, E)
        k3 = h * f(r + 0.5 * k2, x + 0.5 * h, E)
        k4 = h * f(r + k3, x + h, E)
        r = r + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    solve = r[0]
    xpoints = x_points
    wave = wavefunc
    return solve, xpoints, wave


def f(r, x, E):
    const = 26.245869e-4
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = const * (V(x) - E) * psi
    return np.array([fpsi, fphi])


def V(x):
    V0 = 50
    a = 1.0
    return V0 * ((x / a) ** 4)


def simpson_intg(wavefunction):
    L = 10
    N = 2000
    h = (2 * L) / N
    for k in range(1, 4, 1):
        sumx = 0
        points = wavefunction[k - 1][:]
        n = len(points)
        for i in range(2, n, 1):
            if i % 2 == 0:
                sumx = sumx + 4 * (points[i] ** 2)
            else:
                sumx = sumx + 2 * (points[i] ** 2)

        sumx = (h / 3) * ((points[0] ** 2) + (points[n - 1] ** 2) + sumx)
        wavefunction[k - 1][:] = wavefunction[k - 1][:] / sqrt(sumx)
    normalize = wavefunction
    return normalize


for p in range(1, 4, 1):
    E1 = energy_trial[p - 1][0]
    E2 = energy_trial[p - 1][1]
    psi2, a, b = slv(E1)
    target = 1e-12
    itera = 0
    while abs(E1 - E2) > target:
        psi1 = psi2
        psi2, x, wavefunction[p - 1][:] = slv(E2)
        E1_cp = E1
        E1 = E2
        E2 = E2 - (psi2 * (E2 - E1_cp) / (psi2 - psi1))
        itera = itera + 1
        er = abs(psi1 - psi2)
    energy[p - 1] = E2

print('The first 3 energy levels are:', energy, 'in eV.')

wavefunc = simpson_intg(wavefunction)

for p in range(1, 4, 1):
    plt.plot(x[500:1500], wavefunc[p - 1][500:1500], label=p)
plt.xlabel('x')
plt.ylabel('psi')
plt.legend()
plt.show()
