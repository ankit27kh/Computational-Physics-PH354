'''
Ankit Khandelwal
15863
Home Work 7
Exercise 6
'''

from math import exp

a = 2227057010910366687
M = 2**64 - 59

N = 1000000

x1 = 136545681 #seed

n = 0
rand_x = []

def w(x):
    return x**(-1/2)

def f(x):
    return x**(-1/2)/(exp(x)+1)

while n < N:
    x1 = int(a*x1)%M
    y1 = x1/(M-1)
    rand_x.append(y1**2)
    n = n + 1

summ = 0
for i in range(1,N,1):
    summ = summ + f(rand_x[i-1])/w(rand_x[i-1])

I = 2/N * summ
print('Integral is {}'.format(I))
