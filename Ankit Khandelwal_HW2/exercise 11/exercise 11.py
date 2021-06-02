# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:38:55 2020

@author: Ankit Khandewal
"""
from math import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

altitude = pd.read_csv("altitude.txt", sep=' ', header=None)
stm = pd.read_csv("stm.txt", sep=' ', header=None)

xv = np.linspace(0, 196, 197)
yv = np.linspace(0, 1024, 1025)

Ex = np.zeros((1025, 197))
Ey = np.zeros((1025, 197))

for i in yv:
    for j in xv:
        if j == 196:
            continue
        i1 = int(i)
        j1 = int(j)
        if pd.isnull(altitude[i1][j1 + 1]) or pd.isnull(altitude[i1][j1]):
            continue
        Ex[i1][j1] = (altitude[i1][j1 + 1] - altitude[i1][j1]) / 30000

for j in xv:
    for i in yv:
        if i1 == 1024:
            continue
        i1 = int(i)
        j1 = int(j)
        if pd.isnull(altitude[i1 + 1][j1]) or pd.isnull(altitude[i1][j1]):
            continue
        Ey[i1][j1] = (altitude[i1 + 1][j1] - altitude[i1][j1]) / 30000

Intensity = np.zeros((1025, 197))

for i in yv:
    for j in xv:
        i1 = int(i)
        j1 = int(j)
        if pd.isnull(Ex[i1][j1]) or pd.isnull(Ey[i1][j1]):
            continue
        Intensity[i1][j1] = (cos(radians(45)) * Ex[i1][j1] + sin(degrees(45)) * Ey[i1][j1]) / (
                sqrt(Ex[i1][j1] ** 2 + Ey[i1][j1] ** 2) + 1)

plt.imshow(Intensity.transpose(), cmap='Blues')
plt.title("World")
plt.show()
