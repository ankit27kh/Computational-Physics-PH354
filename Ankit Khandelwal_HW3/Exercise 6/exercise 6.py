"""
Ankit Khandelwal
15863
Exercise 6
"""

from math import exp
import scipy.constants as sc

def f(x):
    return exp(x)*(x-5)+5

a=4
b=5
x=(a+b)/2
while abs(f(x)) > 10**-7:
    if f(a)*f(x) > 0:
        a=x
        b=b
    else:
        a=a
        b=x
    x=(a+b)/2
print(x, 'This is x. Lambda max depends on x and T.\n')

 
b=sc.h*sc.c/x/sc.Boltzmann
print(b, 'Wein\'s Constant\n')

l=502*10**-9
print(b/l, 'Temperature of Sun')
