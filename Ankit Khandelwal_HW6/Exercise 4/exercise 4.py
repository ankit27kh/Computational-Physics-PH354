"""
Home Work 6
Ankit Khandelwal
Exercise 4
15863
"""

import numpy as np
import matplotlib.pyplot as plt

ti = 0
tf = 10
N = 100
error = 10**-6
g = 9.8
h = (tf-ti)/N

tv = np.linspace(ti, tf, N+1)
xv_old = np.zeros((N+1), float)
xv = np.copy(xv_old) 

count = 1
while True:
    for i in range(N):
        if i == 0:
            xv[i] = 0
        else:
            xv[i] = (g*h**2 + xv_old[i-1] + xv_old[i+1])/2
    if abs(np.amax(xv - xv_old)) <= error:
        break
    xv_old = np.copy(xv)
    count = count + 1

plt.plot(tv, xv)
plt.xlabel('Time')
plt.ylabel('Height')
plt.title('Trajectory')
plt.show()
