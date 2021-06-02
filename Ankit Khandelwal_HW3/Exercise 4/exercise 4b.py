"""
Ankit Khandelwal
15863
Exercise 4a,b
"""

import math

import matplotlib.pyplot as plt
import numpy as np


def f(x, c):
    return 1 - math.exp(-c * x)


# part 1
c = 2
x = 1
while abs(x - f(x, c)) > 10 ** -7:
    x = f(x, c)
print(x, 'Value for c = 2')

# part 2
c = np.linspace(0, 3, 301)
ans = []

for i in c:
    x = 1
    while abs(x - f(x, i)) > 10 ** -7:
        x = f(x, i)
    ans.append(x)

plt.plot(c, ans)
plt.xlabel('C')
plt.ylabel('X')
plt.title('Solutions of x = 1 - exp(-cx)')
plt.show()
