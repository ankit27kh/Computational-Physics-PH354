"""
Ankit Khandelwal
15863
Exercise 9
"""

def f(r):
    G = 6.674*10**-11
    M = 5.974*10**24
    m = 7.348*10**22
    R = 3.844*10**8
    w = 2.662*10**-6
    return G*M/r**2 - G*m/(R-r)**2 - w**2*(r)
R = 3.844*10**8
a=0.99*R
b=0.5*R
c = (a*f(b)-b*f(a))/(f(b)-f(a))
while abs(f(c)) > 10**-6:
    a = b 
    b = c
    c = (a*f(b)-b*f(a))/(f(b)-f(a))
print('The value of r for L1 point is (in meteres): ', c)

