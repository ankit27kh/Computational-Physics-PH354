'''
ANKIT KHANDELWAL
15863

Exercise 5
'''

from time import perf_counter_ns

start = perf_counter_ns()
C = []
for i in range(0, 102):
    C.append(i)
C[0] = 1
for i in range(0, 101):
    C[i + 1] = ((4 * i + 2) / (i + 2)) * C[i]
print('C(100) is', C[100])
end = perf_counter_ns()
time_taken = end - start
print('Time taken to run the program is', time_taken, 'nano seconds.')
