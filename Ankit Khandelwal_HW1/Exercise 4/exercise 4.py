'''
ANKIT KHANDELWAL
15863

Exercise 4
'''

import math

import scipy.constants as sc

v1 = int(input('Enter v1 (in m/s): '))
l1 = int(input('Enter l1 (in meters): '))
G = sc.gravitational_constant
M = 1.989 * 10 ** 30
mu = G * M
v2 = mu / v1 / l1 - math.sqrt((4 * mu ** 2 / v1 ** 2 / l1 ** 2) + 4 * (v1 ** 2 - 2 * mu / l1)) / 2
l2 = v1 * l1 / v2
print('\nv2 is:', v2)
print('l2 is:', l2)
e = math.sqrt(l1 ** 2 + l2 ** 2) / (l1 + l2) / 4
print('Eccentricity is :', e)
a = (l1 + l2) / 2
b = math.sqrt(l1 * l2)
T = 2 * math.pi * a * b / (l1 * v1)
print('Time period is:', T / 60 / 60 / 24 / 365, ' years')
