'''
ANKIT KHANDELWAL
15863
Exercise 6
'''

import numpy as np
import pandas as pd

pitch = pd.read_csv("pitch.txt", sep='\t', header=None)
n1 = len(pitch)
pitch_array = np.zeros(n1)
for i in range(n1):
    pitch_array[i] = pitch[0][i]


def FFT(x):
    N = len(x)
    if N == 1:
        return x
    X_even = FFT(x[::2])
    X_odd = FFT(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([X_even + factor[:N // 2] * X_odd, X_even + factor[N // 2:] * X_odd])


c = FFT(pitch_array)
c1 = np.fft.fft(pitch_array)
print(c, 'Using user defined function.\n')
print(c1, 'Using built-in function.\n')

diff = abs(c - c1)
max_error = max(diff)
print(max_error, 'This is the max error between the two.')
