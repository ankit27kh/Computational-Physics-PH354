'''
ANKIT KHANDELWAL
15863
Exercise 2
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from cmath import exp, pi

sunspots = pd.read_csv("sunspots.txt", sep='\t', header=None)
time = sunspots[0]
number = sunspots[1]
plt.plot(time, number)
plt.xlabel('Time')
plt.ylabel('Number of Sunspots')
plt.figure()

t1= time[0:500]
n1= number[0:500]
plt.plot(t1,n1)
plt.xlabel('Time')
plt.ylabel('Number of Sunspots')
plt.title('For approximating period.')
plt.figure()
# Period is around 100 months.

N = 3143
xv=np.arange(0,N)

def dft(y):
    c = np.zeros(N , complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] = c[k] + y[n]*exp(-2j*pi*k*n/N)
    for i in range(1, N//2+1):
        c[N-i] = c[i].conjugate()
    return c

dftnumber = dft(number)

cmod=[]
for i in range(N):
    cmod.append(abs(dftnumber[i])**2)

plt.plot(xv,cmod)
plt.title('Coefficient\'s amplitudes.')
plt.figure()

maxx = cmod[1:100]
xv1 = np.arange(1,100)
plt.plot(xv1,maxx)
plt.title('Coefficient\'s amplitudes.')
plt.show()
# k = 24
# period of the sine wave = N/k ~ 131 months.
