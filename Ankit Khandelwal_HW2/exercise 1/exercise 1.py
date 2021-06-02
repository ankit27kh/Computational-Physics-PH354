'''
ANKIT KHANDELWAL
15863

Exercise 1
'''

import matplotlib.pyplot as plt
import pandas as pd

velocity = pd.read_csv("velocities.txt", sep='\t', header=None)
# print(velocity)
time = velocity[0]
speed = velocity[1]
plt.plot(time, speed, label='Velocity')

y = []
h = 1
I = 0
for i in time:
    if i == 0:
        S = speed[i]
        I = I + S
        I = I * h / 2
        y.append(I)
    else:
        S = speed[i - 1] + speed[i]
        I = I + S
        I = I * h / 2
        y.append(I)

print(I)
plt.plot(time, y, label='Distance')
plt.xlabel('Time')
plt.legend()
plt.show()
