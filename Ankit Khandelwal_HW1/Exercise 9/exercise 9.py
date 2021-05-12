'''
ANKIT KHANDELWAL
15863

Exercise 9
'''

import math

prime=[2]
for n in range(3,10000):
    low_i = int(math.sqrt(n))
    for i in prime:
        if n % i == 0:
            break
        if i > low_i:
            prime.append(n)
            break
print('Prime numbers upto 10000 are:')
print(prime)
