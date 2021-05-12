from math import *
import numpy as np
import matplotlib.pyplot as plt

def simpson(n, fx, a, b):
    h = (b-a)/n
    x_values = np.linspace(a, b, n+1)
    I = 0
    for i in range(0, n-1, 2):
        j = x_values[i]
        S = h/3*(fx(j) + 4*fx(j+h) + fx(j+2*h))
        I = I + S
    return I

def J(m, x):
    def fx(th):
            return cos(m*th - x*sin(th))
    return    1/pi*(simpson(1000, fx, 0, pi))

x_values1 = np.linspace(0, 20, 100)
y1=[]
y2=[]
y3=[]
for i in x_values1:
    y1.append(J(0, i))
    y2.append(J(1, i))
    y3.append(J(2, i))

plt.plot(x_values1, y1, label='J0')
plt.plot(x_values1, y2, label='J1')
plt.plot(x_values1, y3, label='J2')
plt.legend()
plt.xlabel('X')
plt.show()
