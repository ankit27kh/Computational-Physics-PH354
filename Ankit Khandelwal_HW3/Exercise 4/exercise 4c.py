"""
Ankit Khandelwal
15863
Exercise 4c
"""

from math import *

def f(x, c):
    def g(x):
        return 1-exp(-c*x)-x
    r = -exp(1)/(1-exp(1))
    return x + r*g(x)
print('# With acceleration')
c = 2
x = 1
count = 1
while abs(x - f(x, c)) > 10**-7:
    print(count,'----->',x)
    x = f(x, c)
    count +=1
print(count,'----->',x)

print('\n# Without acceleration')
def gx(x, c):
    return 1-exp(-c*x)

c = 2
x = 1
count = 1
while abs(x - gx(x, c)) > 10**-7:
    print(count,'----->',x)
    x = gx(x, c)
    count +=1
print(count,'----->',x)
