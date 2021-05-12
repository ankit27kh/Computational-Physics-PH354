'''
ANKIT KHANDELWAL
15863

Exercise 16
'''

import pandas as pd
import matplotlib.pyplot as plt
import scipy.constants as sc

millikan = pd.read_csv("millikan.txt", sep=' ', header=None)
x = []
y = []
sumx = 0
sumy = 0
sumxx = 0
sumxy = 0
for i in range(0,6):
    x.append(millikan[0][i])
    y.append(millikan[1][i])
for xi in x:
    sumx = sumx + xi
    sumxx = sumxx + xi**2 
for yi in y:
    sumy = sumy + yi
for i in range(0,6):
    sumxy = sumxy + x[i]*y[i]
Ex = sumx/6
Exx = sumxx/6
Ey = sumy/6
Exy = sumxy/6
m = (Exy - Ex*Ey)/(Exx - Ex**2)
c = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)
newy = []
for xi in x:
    newy.append(m*xi + c)
plt.plot(millikan[0], millikan[1], 'k.')
plt.plot(x, newy)
plt.show()
e = 1.602*10**-19
h = m*e
print('Value of h from program is: ', h)
print('Actual value is: ', sc.h)
print('Percent Error is: ', (sc.h - h)/sc.h*100)
