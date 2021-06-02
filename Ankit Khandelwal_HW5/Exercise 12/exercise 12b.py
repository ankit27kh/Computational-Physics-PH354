"""
Home Work 5
Ankit Khandelwal
Exercise 12
15863
"""

from math import sqrt

import matplotlib.pyplot as plt
import numpy as np

G = 1
m1 = 150
m2 = 200
m3 = 250
delta = 10 ** -3


def f(solution):
    r1x = solution[0]
    r2x = solution[1]
    r3x = solution[2]
    rv1x = solution[3]
    rv2x = solution[4]
    rv3x = solution[5]
    r1y = solution[6]
    r2y = solution[7]
    r3y = solution[8]
    rv1y = solution[9]
    rv2y = solution[10]
    rv3y = solution[11]
    fr1x = rv1x
    fr2x = rv2x
    fr3x = rv3x
    fr1y = rv1y
    fr2y = rv2y
    fr3y = rv3y
    r1 = sqrt(r1x ** 2 + r1y ** 2)
    r2 = sqrt(r2x ** 2 + r2y ** 2)
    r3 = sqrt(r3x ** 2 + r3y ** 2)
    frv1x = G * m2 * (r2x - r1x) / abs(r2 - r1) ** 3 + G * m3 * (r3x - r1x) / abs(r3 - r1) ** 3
    frv2x = G * m1 * (r1x - r2x) / abs(r1 - r2) ** 3 + G * m3 * (r3x - r2x) / abs(r3 - r2) ** 3
    frv3x = G * m2 * (r2x - r3x) / abs(r2 - r3) ** 3 + G * m1 * (r1x - r3x) / abs(r1 - r3) ** 3
    frv1y = G * m2 * (r2y - r1y) / abs(r2 - r1) ** 3 + G * m3 * (r3y - r1y) / abs(r3 - r1) ** 3
    frv2y = G * m1 * (r1y - r2y) / abs(r1 - r2) ** 3 + G * m3 * (r3y - r2y) / abs(r3 - r2) ** 3
    frv3y = G * m2 * (r2y - r3y) / abs(r2 - r3) ** 3 + G * m1 * (r1y - r3y) / abs(r1 - r3) ** 3
    return np.array([fr1x, fr2x, fr3x, frv1x, frv2x, frv3x, fr1y, fr2y, fr3y, frv1y, frv2y, frv3y])


ti = 0
tf = 2
h = .1
hh = []
solution = np.array([3, -1, -1, 0, 0, 0, 1, -2, 1, 0, 0, 0], float)
r1xpoints = []
r2xpoints = []
r3xpoints = []
r1ypoints = []
r2ypoints = []
r3ypoints = []
r1xpoints.append(solution[0])
r2xpoints.append(solution[1])
r3xpoints.append(solution[2])
r1ypoints.append(solution[6])
r2ypoints.append(solution[7])
r3ypoints.append(solution[8])
r1xpoints_ = []
r2xpoints_ = []
r3xpoints_ = []
r1ypoints_ = []
r2ypoints_ = []
r3ypoints_ = []
check = solution.copy()
r1xpoints_.append(check[0])
r2xpoints_.append(check[1])
r3xpoints_.append(check[2])
r1ypoints_.append(check[6])
r2ypoints_.append(check[7])
r3ypoints_.append(check[8])
final = solution.copy()
h_min = 10 ** -13 / 11

while ti < tf:
    check_h = 0
    while check_h == 0:
        for t in [ti, ti + h]:
            k1 = h * f(solution)
            k2 = h * f(solution + 0.5 * k1)
            k3 = h * f(solution + 0.5 * k2)
            k4 = h * f(solution + k3)
            solution += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            r1xpoints.append(solution[0])
            r2xpoints.append(solution[1])
            r3xpoints.append(solution[2])
            r1ypoints.append(solution[6])
            r2ypoints.append(solution[7])
            r3ypoints.append(solution[8])
        h = 2 * h
        for t in [ti]:
            k1 = h * f(check)
            k2 = h * f(check + 0.5 * k1)
            k3 = h * f(check + 0.5 * k2)
            k4 = h * f(check + k3)
            check += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            r1xpoints_.append(check[0])
            r2xpoints_.append(check[1])
            r3xpoints_.append(check[2])
            r1ypoints_.append(check[6])
            r2ypoints_.append(check[7])
            r3ypoints_.append(check[8])
        h = h / 2
        e1 = 1 / 30 * (r1xpoints[-1] - r1xpoints_[-1])
        e2 = 1 / 30 * (r2xpoints[-1] - r2xpoints_[-1])
        e3 = 1 / 30 * (r3xpoints[-1] - r3xpoints_[-1])
        e4 = 1 / 30 * (r1ypoints[-1] - r1ypoints_[-1])
        e5 = 1 / 30 * (r2ypoints[-1] - r2ypoints_[-1])
        e6 = 1 / 30 * (r3ypoints[-1] - r3ypoints_[-1])
        error = sqrt(e1 ** 2 + e2 ** 2 + e3 ** 2 + e4 ** 2 + e5 ** 2 + e6 ** 2)
        if error == 0:
            h_new = 1.5 * h
        else:
            h_new = h * (h * delta / error) ** (1 / 4)
        if h_new > 1.5 * h:
            h_new = 1.5 * h
        if h_new < h and h_new > h_min:
            h = h_new
            solution = final.copy()
            check = final.copy()
            r1xpoints.pop(-1)
            r2xpoints.pop(-1)
            r3xpoints.pop(-1)
            r1ypoints.pop(-1)
            r2ypoints.pop(-1)
            r3ypoints.pop(-1)
            r1xpoints.pop(-1)
            r2xpoints.pop(-1)
            r3xpoints.pop(-1)
            r1ypoints.pop(-1)
            r2ypoints.pop(-1)
            r3ypoints.pop(-1)
        elif h_new > h:
            ti = ti + 2 * h
            check_h = 1
            final = solution.copy()
            check = solution.copy()
            h = h_new
        else:
            ti = ti + 2 * h
            check_h = 1
            final = solution.copy()
            check = solution.copy()
            h = h_min
    hh.append(h)

plt.plot(r1xpoints, r1ypoints, 'b.', markersize=1, label='Star 1')
plt.plot(r2xpoints, r2ypoints, 'r.', markersize=1, label='Star 2')
plt.plot(r3xpoints, r3ypoints, 'g.', markersize=1, label='Star 3')
plt.xlabel('X')
plt.ylabel('Y')
plt.yscale('symlog')
plt.xscale('symlog')
plt.xticks((-10 ** 12, -10 ** 8, -10 ** 4, -10, 10, 10 ** 4, 10 ** 8, 10 ** 12))
plt.yticks((-10 ** 12, -10 ** 8, -10 ** 4, -10, 10, 10 ** 4, 10 ** 8, 10 ** 12))
plt.title('Log Trajectory')
plt.legend(loc='lower left')
plt.show()
