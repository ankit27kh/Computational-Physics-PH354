"""
Home Work 6
Ankit Khandelwal
Exercise 2
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin

D = 0.1
A = 10
B = 12
tau = 365

def T_surf(t):
    return A + B * sin(2*pi*t/tau)

L = 20
N = 40
a = L/N
h = 1

Temp = np.zeros(N, float)
Temp[0] = T_surf(0)
Temp[1:N-1] = 10
Temp[N-1] = 11 
Temp_new = np.zeros((N), float)
xv = np.linspace(0,20,N)

for t in range(10*365):
    for x in range(N):
        if x == 0:
            Temp_new[x] = T_surf(t)
        elif x < N-1:
            Temp_new[x] = Temp[x] + h*D/a**2 * (Temp[x+1] + Temp[x-1] - 2*Temp[x])
        else:
            Temp_new[x] = 11
        Temp = np.copy(Temp_new)
    if t == 91+9*365/h or t == 182+9*365/h or t == 273+9*365/h or t == 364+9*365/h:
        plt.plot(xv, Temp, label='{0:.2f} years.'.format((t/365)))
plt.legend()
plt.xlabel('Depth (in m)')
plt.ylabel('Temperature (in C)')
plt.title('Temperature Profile of Earth\'s Crust')
plt.show()
