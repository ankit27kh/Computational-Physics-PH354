"""
Ankit Khandelwal
15863
Exercise 1
"""

import numpy as np
from cmath import sin, exp, pi
import matplotlib.pyplot as plt

N = 1000
xv=np.linspace(0,1,N)

def f1(x):
    if x < 0.5:
        return -0.5
    else:
        return 0.5

def f2(x):
    return x

def f3(x):
    return sin(pi*x/N)*sin(20*pi*x/N)

def dft(y):
    c = np.zeros(N , complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] = c[k] + y[n]*exp(-2j*pi*k*n/N)
    for i in range(1, N//2+1):
        c[N-i] = c[i].conjugate()
    return c

yv1=[]
yv2=[]
yv3=[]

for i in xv:
    yv1.append(f1(i))
    yv2.append(f2(i))
    yv3.append(f3(i))

dftf1=dft(yv1)
dftf2=dft(yv2)
dftf3=dft(yv3)

c1mod=[]
c2mod=[]
c3mod=[]
for i in range(N):
    c1mod.append(abs(dftf1[i]))
    c2mod.append(abs(dftf2[i]))
    c3mod.append(abs(dftf3[i]))

plt.figure()
plt.plot(xv,c1mod)
plt.title('Square Wave coefficient\'s amplitudes.')
plt.figure()
plt.plot(xv,c2mod)
plt.title('Saw Tooth coefficient\'s amplitudes.')
plt.figure()
plt.plot(xv,c3mod)
plt.title('Modulated Sine Wave coefficient\'s amplitudes.')
plt.show()