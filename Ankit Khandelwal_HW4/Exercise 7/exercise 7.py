'''
ANKIT KHANDELWAL
15863
Exercise 7
'''

import numpy as np
from math import sin, sqrt, pi
import matplotlib.pyplot as plt

def q(u):
    alpha = pi/(20*10**-6)
    return sin(alpha*u)**2

def y(u):
    return sqrt(q(u))

w = 200*10**-6
W = 10*w
wavelength = 500*10**-9
f = 1
n = 40
N = 10*n
xv = np.arange(n)
u = xv*w/n - w/2
yv = np.zeros(40)

for i in xv:
    yv[i] = y(u[i])

extra = np.zeros(N-n)
yv = np.concatenate((yv, extra))

c = np.fft.fft(yv)
cmod = abs(c)**2
Intensity = W**2/N**2 * cmod
Intensity = Intensity[:201]
Intensity = np.concatenate((np.zeros(200), Intensity))

for i in range(200):
    Intensity[i] = Intensity[-i-1]

xvalue = np.linspace(-5, 5, N+1)
plt.plot(xvalue, Intensity)
plt.title('Diffraction Pattern')
plt.xlabel('Distance (in cm)')
plt.ylabel('Intensity')
plt.show()
