"""
Home Work 5
Ankit Khandelwal
Exercise 1
15863
"""

import numpy as np
import matplotlib.pyplot as plt
 
def Vin(t):
    if int(2*t)%2 == 0:
        return 1
    else:
        return -1

for RC in (0.01, 0.1, 1):
    def f(V, t):
        return 1/RC * (Vin(t) - V)
    
    ti = 0.0
    tf = 10.0
    N = 1000
    h = (tf- ti)/N
    tv = np.arange(ti, tf, h)
    xv = []
    x = 0.0
    
    for t in tv:
        xv.append(x)
        k1 = h*f(x, t)
        k2 = h*f(x + 0.5* k1 , t+ 0.5* h)
        k3 = h*f(x + 0.5* k2 , t+ 0.5* h)
        k4 = h*f(x + k3 , t+ h)
        x += (k1 +2*k2 + 2*k3 + k4)/6
    plt.plot(tv, xv, label=RC)
plt.legend(loc='upper right')
plt.xlabel('Time')
plt.ylabel('Vout')
plt.show()
