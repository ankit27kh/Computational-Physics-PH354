'''
ANKIT KHANDELWAL
15863

Exercise 3
'''

import scipy.constants as sc
import math

m = 9.11*10**(-31) 
E = 10
V = 9
k1 = math.sqrt(2*m*E)/sc.hbar
k2 = math.sqrt(2*m*(E-V))/sc.hbar
T = 4*k1*k2/((k1+k2)**2)
R = ((k1-k2)/(k1+k2))**2
print('Transmission probability is:', T)
print('Reflection probability is:', R)
