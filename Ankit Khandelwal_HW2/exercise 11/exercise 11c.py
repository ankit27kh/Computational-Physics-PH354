# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:31:35 2020

@author: Ankit Khandewal
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

stm = pd.read_csv("stm.txt", sep=' ', header=None)

xv = np.linspace(0, 473, 474)
yv = np.linspace(0, 675, 676)

Ex=np.zeros((676,474))
Ey=np.zeros((676,474))

for i in yv:
    for j in xv:
        if j == 473:
            continue
        i1=int(i)
        j1=int(j)
        if pd.isnull(stm[i1][j1+1]) or pd.isnull(stm[i1][j1]):
            continue
        Ex[i1][j1] = (stm[i1][j1+1] - stm[i1][j1])/2.5

for j in xv:
    for i in yv:
        if i1 == 675:
            continue
        i1=int(i)
        j1=int(j)
        if pd.isnull(stm[i1+1][j1]) or pd.isnull(stm[i1][j1]):
            continue
        Ey[i1][j1] = (stm[i1+1][j1] - stm[i1][j1])/2.5

Intensity = np.zeros((676,474))

for i in yv:
    for j in xv:
        i1=int(i)
        j1=int(j)
        if pd.isnull(Ex[i1][j1]) or pd.isnull(Ey[i1][j1]):
            continue
        Intensity[i1][j1] = ( cos(radians(45)) * Ex[i1][j1] + sin(degrees(45)) * Ey[i1][j1] )/(sqrt(Ex[i1][j1]**2 + Ey[i1][j1]**2) + 1) 

plt.imshow(Intensity.transpose(), cmap='Blues')
plt.title("Silicon Surface")
plt.show()