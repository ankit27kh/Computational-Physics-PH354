'''
ANKIT KHANDELWAL
15863
Exercise 4
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dow = pd.read_csv("dow.txt", sep='\n', header=None)
N=1024
d =[]
for i in range(1024):
    d.append(dow[0][i])
plt.plot(np.arange(0,N),d, label='Original')

dow_fft = np.fft.rfft(d)
for i in range(51,513):
    dow_fft[i] = 0
inverse = np.fft.irfft(dow_fft)
plt.plot(np.arange(0,N),inverse, label='Smooth 10%')

for i in range(20,513):
    dow_fft[i] = 0
inverse = np.fft.irfft(dow_fft)
plt.plot(np.arange(0,N),inverse, label='Smooth 2%')
plt.legend()

'''
We can see that the curve gets smoothened out when we set
coefficients to zero. The 'smoothness' increases when we set
more coefficients to zero.
Smoothening is because we are setting higher frequency modes to zero.
'''
