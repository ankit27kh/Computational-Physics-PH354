'''
ANKIT KHANDELWAL
15863

Exercise 11c
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sunspots = pd.read_csv("sunspots.txt", sep='\t', header=None)
time = sunspots[0][:1000]
number = sunspots[1][:1000]
number1 = [0, 0, 0, 0, 0]
time1 = []
for i in range(0,1000):
    time1.append(time[i])
    number1.append(number[i])
for i in range(1,6):
    number1.append(0)
r = 5
Y = np.linspace(0, 999, 1000)
for k in range(5,1005):
    sum = 0
    for m in range(-r, r + 1):
        sum = sum + number1[k + m]
    Y[k-5] = sum/2/r

plt.plot(time, number, label='Original')
plt.plot(time1, Y, 'k', label='Average')
plt.xlabel('Time')
plt.ylabel('Number of Sunspots')
plt.legend()
plt.show()
