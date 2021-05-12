'''
ANKIT KHANDELWAL
15863

Exercise 11b
'''

import pandas as pd
import matplotlib.pyplot as plt

sunspots = pd.read_csv("sunspots.txt", sep='\t', header=None)
time = sunspots[0][:1000]
number = sunspots[1][:1000]
plt.plot(time, number)
plt.xlabel('Time')
plt.ylabel('Number of Sunspots')
plt.show()
