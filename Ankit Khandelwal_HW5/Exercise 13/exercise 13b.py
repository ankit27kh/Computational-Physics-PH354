"""
Home Work 5
Ankit Khandelwal
Exercise 13b
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

n = 3 

def f(solution, C):
    m = solution[0]
    th = solution[1]
    fm = C**2*th**n
    fth = -m/C**2 
    return np.array([fm, fth])

Ci = 0 
Cf = 3
h = 0.001
Cpoints = np.arange(Ci+h, Cf, h)

for i in range(1,8,1):
    mpoints = []
    thpoints = []
    solution = np.array([0, i], float)    
    for c in Cpoints:
        mpoints.append(solution[0])
        thpoints.append(solution[1])
        k1 = h*f(solution, c)
        k2 = h*f(solution+0.5*k1, c+0.5*h) 
        k3 = h*f(solution+0.5*k2, c+0.5*h) 
        k4 = h*f(solution+k3, c+h)
        solution += (k1 + 2*k2 + 2*k3 + k4 )/6
    plt.plot(Cpoints, thpoints, label=i)
plt.xlabel('C')
plt.ylabel('Theta')
plt.legend()
plt.grid()

i = 7
while thpoints[1999]>10**-5 or thpoints[1999]<-10**-5:
    i = i - thpoints[1999]/(-mpoints[1999]/4)
    mpoints = []
    thpoints = []
    solution = np.array([0, i], float)    
    for c in Cpoints:
        mpoints.append(solution[0])
        thpoints.append(solution[1])
        k1 = h*f(solution, c)
        k2 = h*f(solution+0.5*k1, c+0.5*h) 
        k3 = h*f(solution+0.5*k2, c+0.5*h) 
        k4 = h*f(solution+k3, c+h)
        solution += (k1 + 2*k2 + 2*k3 + k4 )/6
#print(i)
plt.figure()
plt.plot(Cpoints, thpoints, label=i)
plt.xlabel('C')
plt.ylabel('Theta')
plt.legend()
plt.grid()
plt.show()
