"""
Ankit Khandelwal
15863
Exercise 8
"""

import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 1, 101)
y=[]

for i in x_values:
    y.append(924*i**6 - 2772*i**5 + 3150*i**4 - 1680*i**3 + 420*i**2 - 42*i +1)
plt.plot(x_values, y)
plt.grid()


A=[0.0,0.2,0.4,0.6,0.8,1.0]

def der(x):
    h=0.001
    return (fx(x+h) - fx(x))/h

def fx(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x +1

X=[]

for guess in A:
    while abs(fx(guess)) > 10**-11:
        guess = guess - fx(guess)/der(guess)
    X.append(guess)
print('The solutions are: ',X)

for i in X:
    plt.scatter(i, 0)
plt.xlabel('X')
plt.ylabel('f(x)')
plt.show()