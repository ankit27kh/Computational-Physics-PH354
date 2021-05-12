"""
Ankit Khandelwal
15863
Exercise 3
"""

def f(x):
    return x*(x-1)

def der(fx, delta, a):
    return (f(a+delta) - f(a))/delta

a=1

for i in (2,4,6,8,10,12,14):
    delta = 10**-i
    print(delta, '----->', der(f, delta, a))
