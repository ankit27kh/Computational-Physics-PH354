"""
Home Work 5
Ankit Khandelwal
Exercise 7
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import cos

m =1
k = 6
w = 2
N = 5
C = np.zeros((N))
CC = np.zeros((N))
fC = np.zeros((N))
fCC = np.zeros((N))

def ef(t):
    return cos(w*t)

def f(r, t):
    for i in range(N):
        C[i] = r[i]
        CC[i] = r[i+N]
        fC[i] = CC[i]
        if i == 0:
            fCC[i] = k*(C[i+1]-C[i]) + ef(t)
        elif i == N-1:
            fCC[i] = k*(C[i-1]-C[i])
        else:
            fCC[i] = k*(C[i+1] - C[i]) + k*(C[i-1] - C[i])
    return np.concatenate((fC, fCC))

ti = 0
tf = 20
n = 1000
h = (tf- ti)/n
tpoints = np.arange(ti, tf, h)

Cvalues = np.zeros((N, n), float)
CCvalues = np.zeros((N, n), float)
r = np.zeros((2*N), float)


for t in range(n):
    for i in range(N):
        Cvalues[i][t] = r[i]
        CCvalues[i][t] = r[i+N]
        k1 = h*f(r, tpoints[t])
        k2 = h*f(r+0.5*k1, tpoints[t]+0.5*h) 
        k3 = h*f(r+0.5*k2, tpoints[t]+0.5*h) 
        k4 = h*f(r+k3, tpoints[t]+h)
        r += (k1 + 2*k2 + 2*k3 + k4 )/6
        
for i in range(N):
    plt.plot(tpoints, Cvalues[i][:], label=i+1)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.show()
