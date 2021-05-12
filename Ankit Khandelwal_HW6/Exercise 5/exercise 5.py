"""
Home Work 6
Ankit Khandelwal
Exercise 5
15863
"""

from math import exp
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded
import cmath
from matplotlib import animation as animation

M = 9.1*10**-31
L = 10**-8
x0 = L/2
k = 5*10**10
sigma = 10**-10
N = 1000
a = L/N
h = 10**-18
hbar = 1.055*10**-34

B = np.zeros((N-2,N-2), complex)
a1 = 1 + h*hbar*1j/2/M/a**2
a2 = - h*hbar*1j/4/M/a**2
b1 = 1 - h*hbar*1j/2/M/a**2
b2 = h*hbar*1j/4/M/a**2

for i in range(N-2):
    if i < N-3:
        B[i+1][i] = b2
        B[i][i+1] = b2
    B[i][i] = b1

def psi0(x):
    return exp(-(x-x0)**2/(2*sigma**2)) * cmath.exp(k*x*1j)

A_banded = np.zeros((3,N-2), complex)
A_banded[0,1:] = a2
A_banded[1,:] = a1
A_banded[2,:N-3] = a2
xv = np.linspace(a,L-a,N-2)

PSI = np.zeros((N-2), complex)
for i in range(N-2):
    PSI[i] = psi0(xv[i])

v = B@PSI
PSI = solve_banded((1,1), A_banded, v, overwrite_b =True, check_finite=False)
psi_real = PSI.real
frame = 4000
fig, ax = plt.subplots(figsize=(6,4))
line = ax.plot(xv, psi_real)[0]
def animate(i):
    global PSI
    v = B@PSI
    PSI = solve_banded((1,1), A_banded, v, overwrite_b =True, check_finite=False)
    psi_real = PSI.real
    line.set_ydata(psi_real)
    if i == frame-1:
        PSI = np.zeros((N-2), complex)
        for ii in range(N-2):
            PSI[ii] = psi0(xv[ii])
    return line
anim = animation.FuncAnimation(fig,animate,frames=frame,interval=1)
ax.set_xlabel('X')
ax.set_ylabel('Psi')
plt.show()
#anim.save('exercise 5.mp4')
