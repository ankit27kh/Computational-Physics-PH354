"""
Ankit Khandelwal
15863
Exercise 12
"""

import numpy as np
from math import sqrt

n=200
B = 2 * np.diag(np.full(n,1.0)) + np.random.rand(n, n)/sqrt(n)
B_trans = B.transpose()
A = 1/2*(B + B_trans)
print('A : \n', A)
b=np.ones(n).T
print('\nb : \n', b)

#GAussian Elimination
L=np.ones(n).T
U=A.copy()
U=np.c_[U,L]

for i in range(n):
    coloumn = []
    for j in range(i,n):
        coloumn.append(U[j][i])
    value = max(coloumn)
    index = coloumn.index(value)
    U[[i,index+i],:]=U[[index+i,i],:]
    if i < n-1:
        for j in range(i+1,n):
            umul = (U[j][i]/U[i][i])
            U[[j],:]=U[[j],:] - umul*U[[i],:]

for i in range(n):
    U[[i],:]=U[[i],:]/U[i][i]

for i in range(n-1,-1,-1):
    if i > 0:
        for j in range(0,i):
            umul = U[j][i]/U[i][i]
            U[[j],:]=U[[j],:] - umul*U[[i],:]

x=[]
for i in range(n):
    x.append(U[i][n])
print('\nSolution using Gaussian Elimination is :\n', x)

# QR Decomposition
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
y=Q.T@b

x_QR=np.ones(n).T
for i in range(n-1,-1,-1):
    x_QR[i]=(y[i]-((r[[i],:]@x_QR)-r[i][i]))/r[i][i]

print('\nSolution using QR Decomposition is :\n', x_QR)
