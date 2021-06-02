'''
ANKIT KHANDELWAL
15863

Exercise 10
'''

# 10a
from time import perf_counter_ns


def catalan(n):
    if n == 0:
        return 1
    else:
        return ((4 * n - 2) / (n + 1)) * catalan(n - 1)


start = perf_counter_ns()
print('C[100] is', catalan(100))
end = perf_counter_ns()
t = end - start
print('Time taken is:', t, 'nano seconds.')


# 10b
def g(m, n):
    if n == 0:
        return m
    else:
        return g(n, m % n)


print('\ng(108, 192) is:', g(108, 192))
