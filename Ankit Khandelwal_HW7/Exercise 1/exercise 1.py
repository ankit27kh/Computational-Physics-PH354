'''
Ankit Khandelwal
15863
Home Work 7
Exercise 1
'''

import numpy as np

a = 2227057010910366687
M = 2 ** 64 - 59
c = 0

N = 1000000

x1 = np.zeros(N + 1)
y1 = np.zeros(N + 1)
z1 = np.zeros(N, int)
x2 = np.zeros(N + 1)
y2 = np.zeros(N + 1)
z2 = np.zeros(N, int)

A = 1
B = 7

x1[0] = 50561564637  # seed
x2[0] = 60321658795  # seed

for i in range(1, N + 1, 1):
    x1[i] = int(a * x1[i - 1] + c) % M
    y1[i] = x1[i] / (M - 1)
    z1[i - 1] = A + (B - A) * y1[i]
    x2[i] = int(a * x2[i - 1] + c) % M
    y2[i] = x2[i] / (M - 1)
    z2[i - 1] = A + (B - A) * y2[i]
six1 = np.count_nonzero(z1[:] == 6)
six2 = np.count_nonzero(z2[:] == 6)

count = 0
for i in range(N):
    if z1[i] == z2[i] and z1[i] == 6:
        count = count + 1
print('Experimental fraction of double 6 = {} and theoretical = {}'.format(count / N, 1 / 36))
