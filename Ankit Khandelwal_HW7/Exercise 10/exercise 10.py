'''
Ankit Khandelwal
15863
Home Work 7
Exercise 10
'''

from math import acos, pi

a = 2227057010910366687
M = 2**64 - 59
x1 = 5614367 #seed
x2 = 9175135 #seed

x1 = int(a*x1)%M
y1 = x1/(M-1)
theta = (acos(1-2*y1))

x2 = int(a*x2)%M
y2 = x2/(M-1)
phi = (2*pi*y2)
