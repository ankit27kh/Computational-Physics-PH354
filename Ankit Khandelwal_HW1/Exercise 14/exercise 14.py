'''
ANKIT KHANDELWAL
15863

Exercise 14
'''

import matplotlib.pyplot as plt
import numpy as np

r = np.arange(1, 4, 0.01)
x = 0.5
x1 = []
i1 = []
for i in r:
    for j in range(1,1000):
        x = i*x*(1-x)
    for j in range(1,1000):
        x = i*x*(1-x)
        x1.append(x)
        i1.append(i)
    plt.plot(i1, x1, 'k.', markersize=0.02)
    x1 = []
    i1 = []
    x = 0.5
plt.xlabel('r')
plt.ylabel('x')
plt.title('Feigenbaum Plot')
plt.show()
'''
A fixed point will look like a single point on the y-axis as by definition it is a point
which has reached a fixed value.

A limit cycle will show branched behaviour as can be seen from r = 3.0 to 3.5 in the graph.

Chaos will look like continuous lines on the graph.

The edge of chaos here is somewhere close to r = 3.5 where branching stops.
''' 