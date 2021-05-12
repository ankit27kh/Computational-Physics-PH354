'''
Ankit Khandelwal
15863
Home Work 7
Exercise 4
'''

import numpy as np
from math import sin, sqrt

def f(x):
    return sin(1/(x*(2-x)))**2

a = 2227057010910366687
M = 2**64 - 59
c=0

N = 10000
area = 2

x1 = np.zeros(N+1)
y1 = np.zeros(N+1)
z1 = np.zeros(N)
x2 = np.zeros(N+1)
y2 = np.zeros(N+1)
z2 = np.zeros(N)
x3 = np.zeros(N+1)
y3 = np.zeros(N+1)
z3 = np.zeros(N)

X0 = 0
X1 = 2
Y0 = 0
Y1 = 1

x1[0] = 154968415 #seed
x2[0] = 25163788741 #seed
x3[0] = 3135897647 #seed

for i in range(1,N+1,1):
    x1[i] = int(a*x1[i-1]+c)%M
    y1[i] = x1[i]/(M-1)
    z1[i-1] = X0 + (X1-X0)*y1[i]
    x2[i] = int(a*x2[i-1]+c)%M
    y2[i] = x2[i]/(M-1)
    z2[i-1] = Y0 + (Y1-Y0)*y2[i]
    x3[i] = int(a*x3[i-1]+c)%M
    y3[i] = x3[i]/(M-1)
    z3[i-1] = X0 + (X1-X0)*y3[i]

k = 0
summ = 0
summ_2 = 0
for i in range(N):
    summ = summ + f(z3[i])
    summ_2 = summ_2 + f(z3[i])**2
    if z2[i] <= f(z1[i]):
        k = k+1
I1 = k*area/N
I2 = 2/N*summ
var1 = N*(I1/area)*(1-I1/area)
e1 = sqrt(var1)*area/N
var2 = summ_2/N - (summ/N)**2
e2 = (2)*sqrt(var2)/sqrt(N)
print('From hit and miss, I = {}, error = {}'.format(I1, e1))
print('From mean value, I = {}, error = {}'.format(I2, e2))
