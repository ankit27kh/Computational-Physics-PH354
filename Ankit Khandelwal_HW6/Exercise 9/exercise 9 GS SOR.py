"""
Home Work 6
Ankit Khandelwal
Exercise 9 GS SOR
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import exp

xv = np.linspace(-1,1,40)
yv = np.linspace(-1,1,40)

delta = 2/39

def rho(x,y):
    if x <= 0.3 and x >= -0.3:
        return exp(-abs(y)/0.1)
    else:
        return 0
ww = [0.5, 1.5, 2/(1+np.pi/40)]

for w in ww:
    pot = np.zeros((40,40), float)
    error = []
    for t in range(1,1001,1):
        pot_old = np.copy(pot)
        for i in range(40):
            for j in range(40):
                if i != 39 and j != 39:
                    pot[i][j] = (w/4)*((pot[i+1][j] + pot[i-1][j] + pot[i][j+1] + pot[i][j-1]) \
                            - delta**2 * rho(xv[i], yv[j])) + (1-w)*pot[i][j]
                if i == 39 and j != 39:
                    pot[i][j] = (w/4)*((pot[0][j] + pot[i-1][j] + pot[i][j+1] + pot[i][j-1]) \
                            - delta**2 * rho(xv[i], yv[j])) + (1-w)*pot[i][j]
                if i != 39 and j == 39:
                    pot[i][j] = (w/4)*((pot[i+1][j] + pot[i-1][j] + pot[i][0] + pot[i][j-1]) \
                            - delta**2 * rho(xv[i], yv[j])) + (1-w)*pot[i][j]
                if i == 39 and j == 39:
                    pot[i][j] = (w/4)*((pot[0][j] + pot[i-1][j] + pot[i][0] + pot[i][j-1]) \
                            - delta**2 * rho(xv[i], yv[j])) + (1-w)*pot[i][j]
        if t in [10,100,1000]:
            plt.figure()
            plt.contourf(xv, yv, pot, levels=20)
            plt.colorbar()
            plt.title('{}th iterations with w = {}'.format(t, w))
            plt.xlabel('x')
            plt.ylabel('Y')
        error.append(abs(pot - pot_old).sum()/40**2)
    plt.figure()
    plt.plot(error)
    plt.title(w)
    plt.xlabel('Iteration')
    plt.ylabel('Error')
plt.show()
