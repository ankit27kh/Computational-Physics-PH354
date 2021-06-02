'''
ANKIT KHANDELWAL
15863
Exercise 3
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.fft import fft as FFT

piano = pd.read_csv("piano.txt", sep='\n', header=None)
trumpet = pd.read_csv("trumpet.txt", sep='\n', header=None)

n1 = len(piano)
piano_array = np.zeros(n1)
trumpet_array = np.zeros(n1)
for i in range(n1):
    trumpet_array[i] = trumpet[0][i]
    piano_array[i] = piano[0][i]

xv = np.arange(0, n1)
plt.plot(xv, piano)
plt.figure()
plt.plot(xv, trumpet)
plt.figure()

cpiano = FFT(piano_array)
ctrumpet = FFT(trumpet_array)
xv1 = np.arange(0, 10000)

cpiano_mod = abs(cpiano[0:10000])
ctrumpet_mod = abs(ctrumpet[0:10000])
plt.plot(xv1, cpiano_mod)
plt.figure()
plt.plot(xv1, ctrumpet_mod)
plt.figure()

c1 = abs(cpiano[:10000]) ** 2
c2 = abs(ctrumpet[:10000]) ** 2
plt.plot(xv1, c1)
plt.figure()
plt.plot(xv1, c2)
plt.xticks([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000])
plt.show()
f1 = np.argmax(c1)
print('\n', f1 * 44100 / n1, 'Frequency played by Piano')
print('Note be Piano -> C5\n')
f21 = np.argmax(c2[: 3000])
print(f21 * 44100 / n1, 'Frequency played by Trumpet')
print('Note by Trumpet -> C6')

'''
We note that a trumpet is played one note higher to match with the paino.
Also, we note that frequencies for the trumpet are more pronounced than for the piano.
'''
