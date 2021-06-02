'''
ANKIT KHANDELWAL
15863
Exercise 8
'''

from math import exp

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

blur = pd.read_csv("blur.txt", sep=' ', header=None)


def G(x, y):
    return exp(-(x ** 2 + y ** 2) / (2 * 25 ** 2))


gauss = np.ones((1024, 1024))
for i in range(1024):
    for j in range(1024):
        gauss[i - 512][j - 512] = G(i - 512, j - 512)

plt.imshow(blur)
plt.title('Blur')
plt.figure()
plt.imshow(gauss)
plt.title('Gauss')
plt.figure()
blur_fft = np.fft.rfft2(blur)
gauss_fft = np.fft.rfft2(gauss)
unblur = np.ones((1024, 513), complex)

for i in range(1024):
    for j in range(513):
        if gauss_fft[i][j] > 10 ** -3:
            unblur[i][j] = blur_fft[i][j] / gauss_fft[i][j] / 1024 ** 2
        else:
            unblur[i][j] = blur_fft[i][j] / 1024 ** 2

unblur_fft = np.fft.irfft2(unblur)
plt.imshow(unblur_fft)
plt.title('Un-Blur')
plt.show()

'''
There are two reasons limiting our ability to un-blur a photo:
    1. We don't always know the point spread function (PSF).
    2. Even when we approximate the PSF, we can not get arbitrary accuracy
       as we can not divide by very small numbers (or zero) which we get 
       from FFT of the PSF.
'''
