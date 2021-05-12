'''
ANKIT KHANDELWAL
15863

Exercise 6
'''

from time import perf_counter
import math

start = perf_counter()
L = 148
M = 0
for i in range(-L,L):
    for j in range(-L,L):
        for k in range(-L,L):
            if i == 0 and j == 0 and k == 0:
                continue
            if (i+j+k) % 2 == 0:    
                M = 1/(math.sqrt(i**2 + j**2 + k**2)) + M
            else:
                M = -1/(math.sqrt(i**2 + j**2 + k**2)) + M
end = perf_counter()
time = end-start
print('Time to run program is:', time, 'seconds.')
print('The Madelung constant is:', M)
