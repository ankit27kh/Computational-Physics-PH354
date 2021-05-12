'''
ANKIT KHANDELWAL
15863
Exercise 5
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dow2 = pd.read_csv("dow2.txt", sep='\n', header=None)
N=1024
d =[]
for i in range(1024):
    d.append(dow2[0][i])
plt.plot(np.arange(0,N),d, label='Original')
dow_fft = np.fft.rfft(d)

for i in range(20,513):
    dow_fft[i] = 0
inverse = np.fft.irfft(dow_fft)
plt.plot(np.arange(0,N),inverse, label='Smooth 2%')

def dct(y):
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[:N] = y[:]
    y2[N:] = y[::-1]
    c = np.fft.rfft(y2)
    phi = np.exp(-1j*np.pi*np.arange(N)/(2*N))
    return np.real(phi*c[:N])

def idct(a):
    N = len(a)
    c = np.empty(N+1,complex)
    phi = np.exp(1j*np.pi*np.arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return np.fft.irfft(c)[:N]

d_cosine = dct(d)
for i in range(20,513):
    d_cosine[i] = 0
dcos_inv = idct(d_cosine)
plt.plot(np.arange(0,N), dcos_inv, label='Smooth 2% (Cosine)')
plt.legend()
plt.show()