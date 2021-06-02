'''
ANKIT KHANDELWAL
15863

Exercise 11a
'''

import matplotlib.pyplot as plt
import pandas as pd

sunspots = pd.read_csv("sunspots.txt", sep='\t', header=None)
time = sunspots[0]
number = sunspots[1]
plt.plot(time, number)
plt.xlabel('Time')
plt.ylabel('Number of Sunspots')
plt.show()
