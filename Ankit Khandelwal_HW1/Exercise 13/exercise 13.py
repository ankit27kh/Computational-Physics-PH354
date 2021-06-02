'''
ANKIT KHANDELWAL
15863

Exercise 13
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

stm = pd.read_csv("stm.txt", sep=' ', header=None)
plt.imshow(stm)
plt.title('Density Plot')
fig = plt.figure()
ax = plt.axes(projection='3d')

x = np.arange(0, 676, 1)
y = np.arange(0, 663, 1)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, stm, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_zlim3d(0, 100)
ax.view_init(60, 35)
fig
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')
ax.set_title('Silicon Surface')

plt.show()
