"""
Home Work 6
Ankit Khandelwal
Exercise 8 Advection Error
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import exp
from scipy.stats import linregress

v = 1

def sqr(x):
    if x >= 0.6 and x <= 0.8: return 1
    else: return 0

def u0(x):
    return exp(-200*(x-0.3)**2) + sqr(x)

NN = [32,64,128,256,512]

ans_lax = []
ans_upwinding = []
ans_lax_wendroff = []
for N in NN:
    dx = 1/N
    dt = 0.5*dx/v
    dis = 1
    xv = np.linspace(0,dis,dis*N)
    tv = np.linspace(0,1,int(1/dt))
    #lax-wendroff
    u = np.zeros(dis*N)
    for i in range(N):
        u[i] = u0(xv[i])
    u_new = np.copy(u)
    for t in tv:
        for i in range(dis*N-1):
                u_half1 = 1/2*(u[i+1] + u[i]) - dt/2/dx * ((u[i+1]) - (u[i]))
                u_half2 = 1/2*(u[i] + u[i-1]) - dt/2/dx * ((u[i]) - (u[i-1]))
                u_new[i] = u[i] - dt/dx * ((u_half1) - (u_half2))
        u = np.copy(u_new)
    ans_lax_wendroff.append(u_new)
    #lax
    u = np.zeros(dis*N)
    for i in range(N):
        u[i] = u0(xv[i])
    u_new = np.copy(u)
    for t in tv:
        for i in range(dis*N-1):
            u_new[i] = (u[i+1] + u[i-1])/2 - v*dt*(u[i+1] - u[i-1])/2/dx
        u = np.copy(u_new)
    ans_lax.append(u_new)
    #upwinding
    u = np.zeros(dis*N)
    for i in range(N):
        u[i] = u0(xv[i])
    u_new = np.copy(u)
    for t in tv:
        for i in range(dis*N-1):
            u_new[i] = -v*(u[i]-u[i-1])/dx * dt + u[i]
        u = np.copy(u_new)
    ans_upwinding.append(u_new)
xpoints = []
ypoints_lax = []
ypoints_upwinding = []
ypoints_lax_wendroff = []

for i in range(len(NN)-1):
    error_lax = 0
    error_lax_wendroff = 0
    error_upwinding = 0
    for j in range(NN[i]):
        error_lax = error_lax + abs(ans_lax[i][j] - ans_lax[i+1][2*j])
        error_lax_wendroff = error_lax_wendroff + abs(ans_lax_wendroff[i][j] - ans_lax_wendroff[i+1][2*j])
        error_upwinding = error_upwinding + abs(ans_upwinding[i][j] - ans_upwinding[i+1][2*j])
    A = plt.scatter(1/NN[i], error_lax/NN[i], c='r', marker='s')
    B = plt.scatter(1/NN[i], error_lax_wendroff/NN[i], c='g', marker='D')
    C = plt.scatter(1/NN[i], error_upwinding/NN[i], c='b', marker='2')
    #print(1/NN[i], error_lax, error_lax_wendroff, error_upwinding)
    xpoints.append(1/NN[i])
    ypoints_lax.append(error_lax/NN[i])
    ypoints_upwinding.append(error_upwinding/NN[i])
    ypoints_lax_wendroff.append(error_lax_wendroff/NN[i])
    plt.legend((A,B,C),('Lax', 'Lax-Wendroff', 'Upwinding'), scatterpoints=1, loc='lower right')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('dx')
    plt.ylabel('Error')
slope_lax = linregress(xpoints,ypoints_lax)[0]
slope_upwinding = linregress(xpoints,ypoints_upwinding)[0]
slope_lax_wendroff = linregress(xpoints,ypoints_lax_wendroff)[0]
plt.show()
