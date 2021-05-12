"""
Ankit Khandelwal
15863
Exercise 10
"""

import numpy as np
from math import exp

i = 3*10**-9
Vt = 0.05
V = 5.
R1 = 1000.
R2 = 4000.
R3 = 3000.
R4 = 2000.

def f1(V1, V2):
    return R2 * (V1 - V) + R1 * V1 + R1*R2*i*(exp((V1 - V2)/Vt) - 1)

def f2(V1, V2):
    return R4 * (V2 - V) + R3 * V2 - R3*R4*i*(exp((V1 - V2)/Vt) - 1)

def df1_x(V1, V2):
    return R2 + R1 + R1 * R2 * i * exp((V1 - V2)/Vt) / Vt

def df1_y(V1, V2):
    return -R1 * R2 * i * exp((V1 - V2)/Vt) / Vt

def df2_x(V1, V2):
    return -R3 * R4 * i * exp((V1 - V2)/Vt) / Vt

def df2_y(V1, V2):
    return R4 + R3 + R3 * R4 * i * exp((V1 - V2)/Vt) / Vt

x1 = 4.
y1 = 2.
f = np.zeros([2, 1])
J = np.zeros([2, 2])
r1 = np.zeros([2, 1])
r1[0, 0] = x1
r1[1, 0] = y1
d = np.ones([2, 1])
while abs(d[0]) > 10**-7 and abs(d[1]) > 10**-7:
    V1 = r1[0, 0]
    V2 = r1[1, 0]
    f[0, 0] = f1(V1, V2)
    f[1, 0] = f2(V1, V2)
    f1x = df1_x(V1, V2)
    f1y = df1_y(V1, V2)
    f2x = df2_x(V1, V2)
    f2y = df2_y(V1, V2)
    J[0, 0] = f2y
    J[0, 1] = -f1y
    J[1, 0] = -f2x
    J[1, 1] = f1x
    J = (1 / (f1x*f2y - f1y*f2x)) * J
    d = np.dot(J, f)
    r1 = r1 - d

print("V1 = ", r1[0, 0], "V\nV2 = ", r1[1, 0], "V")
print("V = V1 - V2 = ", r1[0, 0]-r1[1, 0], "V")
