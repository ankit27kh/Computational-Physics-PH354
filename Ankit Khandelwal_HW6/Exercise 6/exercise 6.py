"""
Home Work 6
Ankit Khandelwal
Exercise 6
15863
"""

from math import exp, sin, cos, pi
import numpy as np
from numpy.fft import rfft, irfft
import matplotlib.pyplot as plt
import cmath
from matplotlib import animation

M = 9.109*10**-31
L = 10**-8
x0 = L/2
k = 5*10**10
sigma = 10**-10
N = 1000
a = L/N
h = 10**-18
hbar = 1.055*10**-34

def dst(y):
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[0] = y2[N] = 0.0
    y2[1:N] = y[1:]
    y2[:N:-1] = -y[1:]
    a = -np.imag(rfft(y2))[:N]
    a[0] = 0.0
    return a

def idst(a):
    N = len(a)
    c = np.empty(N+1,complex)
    c[0] = c[N] = 0.0
    c[1:N] = -1j*a[1:]
    y = irfft(c)[:N]
    y[0] = 0.0
    return y

def psi0(x):
    return exp(-(x-x0)**2/(2*sigma**2)) * cmath.exp(k*x*1j)

xv = np.linspace(0,L,N+1)
PSI_0 = np.zeros((N+1), complex)
for i in range(N):
    PSI_0[i] = psi0(xv[i])

PSI_0_real = PSI_0.real
PSI_0_comp = PSI_0.imag

PSI_0_real_DST = dst(PSI_0_real)
PSI_0_comp_DST = dst(PSI_0_comp)

def coeff(k, t):
    A = PSI_0_real_DST[k] * cos((pi**2 * hbar * k**2)/2/M/L**2*t)
    B = PSI_0_comp_DST[k] * sin((pi**2 * hbar * k**2)/2/M/L**2*t)
    return A - B

frame = 4000
PSI_t = np.ndarray((N-1,frame), np.ndarray)
tv = np.linspace(0,3*10**-15,frame)

for t in range(frame): 
    PSI_t_coeff = np.zeros(N-1, complex)
    for k in range(1,N,1):
        PSI_t_coeff[k-1] = coeff(k,tv[t])
    PSI_t[:,t] = idst(PSI_t_coeff)
fig, ax = plt.subplots(figsize=(6,4))
line = ax.plot(xv[1:N], PSI_t[:,0])[0]

def animate(i):
    line.set_ydata(PSI_t[:,i])
    return line

anim = animation.FuncAnimation(fig,animate,frames=len(tv)-1,interval=1)
ax.set_xlabel('X')
ax.set_ylabel('Psi')
plt.show()
#anim.save('exercise 6.mp4')
