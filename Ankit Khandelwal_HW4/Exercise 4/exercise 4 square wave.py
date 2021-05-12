'''
ANKIT KHANDELWAL
15863
Exercise 4 Square Wave
'''

import matplotlib.pyplot as plt
import numpy as np
from math import floor

def f(t):
    if floor(2*t)%2 == 0:
        return 1
    else:   
        return -1

xv=np.linspace(0,1,1000)
values = []
for i in range(1000):
    values.append(f(xv[i]))
    
plt.plot(xv,values, label='Square Wave')
v_fft = np.fft.rfft(values)
v_fft[10:]=0
v_inverse = np.fft.irfft(v_fft)
plt.plot(xv,v_inverse, label='Smoothing using first 10 coefficients')
plt.legend(loc='lower left', framealpha=0)
plt.show()

'''
As the function must be periodic, it needs to deviate to acheive periodicity.
This results in large fluctuations at end points.
Also, because we are only using 10 modes, we get wiggles in the result.
We need to use more modes to get better result here.
This is because FT is by definition using sines and cosines.
And we are approximating a straight line with these.
'''