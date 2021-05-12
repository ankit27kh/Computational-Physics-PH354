"""
Home Work 6
Ankit Khandelwal
Exercise 3
15863
"""

from math import exp
import numpy as np
import matplotlib.pyplot as plt

sigma = 0.3
L = 1.0
d = 0.1
v = 100
h = 10**-6
N = 100
a = L/N

disp = np.zeros((N), float)
xv = np.linspace(0, 1, N)
velocity = np.zeros((N), float)
tv = np.linspace(0,1,1/h)
for i in range(N):
    velocity[i] = xv[i]*(L-xv[i])/L**2 * exp(-(xv[i]-d)**2/(2*sigma**2))
disp_new = np.copy(disp)
velocity_new = np.copy(velocity)

for t in range(1,90001,1):
    for x in range(N-1):
        if x == 0 :
            disp_new[x] = 0
            velocity_new[x] = 0
        else:
            disp_new[x] = disp[x] + h*velocity[x]
            velocity_new[x] = velocity[x] + h*v**2/a**2 * (disp[x-1] + disp[x+1] - 2*disp[x])
    disp = np.copy(disp_new)
    velocity = np.copy(velocity_new)
    if (2*t)%(3*10**4) == 0:
        plt.figure(1)
        plt.subplot(2,3,int(2*t/10**4/3))
        plt.plot(disp)
        plt.title('{} seconds'.format(t/10**6))
        plt.axis('off')
        plt.figure(t)
        plt.plot(xv, disp)
        plt.title('{} seconds'.format(t/10**6))
        plt.xlabel('x')
        plt.ylabel('Displacement')
plt.show()
