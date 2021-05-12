"""
Home Work 6
Ankit Khandelwal
Exercise 9 Jacobi
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

pot = np.zeros((40,40), float)
error = []
for t in range(1,1001,1):
    pot_old = np.copy(pot)
    for i in range(40):
        for j in range(40):
            if i != 39 and j != 39:
                pot[i][j] = (pot_old[i+1][j] + pot_old[i-1][j] + pot_old[i][j+1] + pot_old[i][j-1])/4 \
                        - delta**2/4 * rho(xv[i], yv[j])
            if i == 39 and j != 39:
                pot[i][j] = (pot_old[0][j] + pot_old[i-1][j] + pot_old[i][j+1] + pot_old[i][j-1])/4 \
                        - delta**2/4 * rho(xv[i], yv[j])
            if i != 39 and j == 39:
                pot[i][j] = (pot_old[i+1][j] + pot_old[i-1][j] + pot_old[i][0] + pot_old[i][j-1])/4 \
                        - delta**2/4 * rho(xv[i], yv[j])
            if i == 39 and j == 39:
                pot[i][j] = (pot_old[0][j] + pot_old[i-1][j] + pot_old[i][0] + pot_old[i][j-1])/4 \
                        - delta**2/4 * rho(xv[i], yv[j])
    if t in [10,100,1000]:
        plt.contourf(xv, yv, pot, levels=10)
        plt.colorbar()
        plt.title('{}th iterations'.format(t))
        plt.xlabel('x')
        plt.ylabel('Y')
        plt.figure()
    error.append(abs(pot - pot_old).sum()/40**2)
plt.plot(error)
plt.xlabel('Iteration')
plt.ylabel('Error')
#plt.ylim(min(error),max(error))
plt.show()
