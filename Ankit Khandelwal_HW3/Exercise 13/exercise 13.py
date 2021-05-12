"""
Ankit Khandelwal
15863
Exercise 13
"""

import numpy as np

A = np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]])
n=4
print(A)
[E,V] = np.linalg.eig(A)
print('\nEigenvalues using inbuilt function are :\n',E)
values=[]
for i in range(n):
    for j in range(n):
        if i !=j:
            values.append(A[i][j])

while abs(max(values)) > 10**-7:
    v=[]
    q=[]
    r=np.zeros((n,n))
    for i in range(n):
        v.append(A[:,[i]])
    for i in range(n):
        r[i][i] = np.linalg.norm(v[i])
        q.append(v[i]/r[i][i])
        for j in range(i+1,n):
            r[i][j] = q[i].T@v[j]
            v[j] = v[j] - r[i][j]*q[i]
    Q=np.zeros((n,1))
    for i in range(n):
        Q=np.c_[Q,q[i]]
    Q=np.delete(Q,0,1)
    A = r@Q
    values=[]
    for i in range(n):
        for j in range(n):
            if i !=j:
                values.append(A[i][j])

e_values=[]
for i in range(n):
    for j in range(n):
        if i ==j:
            e_values.append(A[i][j])
print('\nCalculated eigenvalues are:\n', e_values)
