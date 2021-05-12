'''
Ankit Khandelwal
15863
Home Work 7
Exercise 7
'''

import numpy as np
from math import exp
import matplotlib.pyplot as plt

J = 1
Temp = [1,2,3]
kb = 1
n = 20
final_mag = []
for T in Temp:
    beta = 1/kb/T
    
    a = 2227057010910366687
    M = 2**64 - 59
    x = 6138413 #seed
    
    spin = np.ndarray((n,n), int)
    for i in range(n):
        for j in range(n):
            x = int(a*x)%M
            y = x/(M-1)
            if y < .5:
                spin[i][j] = 1
            else:
                spin[i][j] = -1
    
    energy = 0
    for i in range(n-1):
        energy = energy + -J*(sum(spin[i,:]*spin[i+1,:]))
    for i in range(n-1):
        energy = energy + -J*(sum(spin[:,i]*spin[:,i+1]))
    
    N = 1000000
    x1 = 3436781767 #seed
    x2 = 43668767441 #seed
    x3 = 11576317 #seed
    mag = [np.sum(spin)]
    
    for i in range(N):
        x1 = int(a*x1)%M
        y1 = int(n*x1/(M-1))
        x2 = int(a*x2)%M
        y2 = int(n*x2/(M-1))
        spin[y1][y2] = -spin[y1][y2]
        energy_new = 0 
        for i in range(n-1):
            energy_new = energy_new + -J*(sum(spin[i,:]*spin[i+1,:]))
        for i in range(n-1):
            energy_new = energy_new + -J*(sum(spin[:,i]*spin[:,i+1]))
        delta_E = energy_new - energy
        x3 = int(a*x3)%M
        y3 = (x3/(M-1))
        if y3 > exp(-beta*delta_E):
            spin[y1][y2] = -spin[y1][y2]
            energy = energy
        else:
            energy = energy_new
        mag.append(np.sum(spin))
    final_mag.append(mag)
    plt.figure(T)
    A = plt.imshow(spin)
    plt.title('T = {}'.format(T))
    A.axes.get_xaxis().set_ticks([])
    A.axes.get_yaxis().set_ticks([])
    plt.show()
