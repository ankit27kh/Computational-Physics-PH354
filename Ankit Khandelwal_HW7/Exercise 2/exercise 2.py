'''
Ankit Khandelwal
15863
Home Work 7
Exercise 2
'''

import numpy as np
import matplotlib.pyplot as plt

a = 2227057010910366687
M = 2**64 - 59
c=0
x1 = 13565421 #seed

time = 20000

Bi213 = np.zeros(time+1, int)
Ti = np.zeros(time+1, int)
Pb = np.zeros(time+1, int)
Bi209 = np.zeros(time+1, int)
Bi213[0] = 10000

prob_Bi213 = 1-2**(-1/46/60)
prob_Ti = 1-2**(-1/2.2/60)
prob_Pb = 1-2**(-1/3.3/60)

for i in range (1,time+1,1):
    decay_count = 0
    for j in range(1,Pb[i-1],1):
        x1 = int(a*x1+c)%M
        y1 = x1/(M-1)
        if y1 < prob_Pb:
            decay_count = decay_count + 1
    Pb[i] = Pb[i-1] - decay_count
    Bi209[i] = Bi209[i-1] + decay_count
    decay_count = 0
    for j in range(1,Ti[i-1],1):
        x1 = int(a*x1+c)%M
        y1 = x1/(M-1)
        if y1 < prob_Ti:
            decay_count = decay_count + 1
    Ti[i] = Ti[i-1] - decay_count
    Pb[i] = Pb[i] + decay_count
    decay_count = 0
    decay_Pb = 0
    decay_Ti = 0
    for j in range(1,Bi213[i-1],1):
        x1 = int(a*x1+c)%M
        y1 = x1/(M-1)
        if y1 < prob_Bi213:
            decay_count = decay_count + 1
            x1 = int(a*x1+c)%M
            y1 = x1/(M-1)
            if y1 < .9791:
                decay_Pb = decay_Pb + 1
            else:
                decay_Ti = decay_Ti + 1
    Bi213[i] = Bi213[i-1] - decay_count
    Ti[i] = Ti[i] + decay_Ti
    Pb[i] = Pb[i] + decay_Pb


plt.plot(Bi213,label='Bi213')
plt.plot(Pb,label='Pb')
plt.plot(Ti,label='Ti')
plt.plot(Bi209,label='Bi209')
plt.xlabel('Time in sec')
plt.ylabel('No. of Atoms')
plt.legend()
plt.show()
