'''
ANKIT KHANDELWAL
15863

Exercise 15
'''

import math

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 2000)
y = np.linspace(-2, 2, 2000)
x_final = []
y_final = []
Re_z = 0
Im_z = 0
for Re_c in x:
    for Im_c in y:
        for i in range(0, 100):
            Re_z1 = Re_z ** 2 - Im_z ** 2 + Re_c
            Im_z1 = 2 * Re_z * Im_z + Im_c
            mod_z1 = math.sqrt(Re_z1 ** 2 + Im_z1 ** 2)
            if mod_z1 > 2:
                break
            Re_z = Re_z1
            Im_z = Im_z1
        if mod_z1 < 2:
            x_final.append(Re_c)
            y_final.append(Im_c)
        Re_z = 0
        Im_z = 0
plt.plot(x_final, y_final, 'k.')
plt.xlabel('Real part of c')
plt.ylabel('Imaginary part of c')
plt.show()
