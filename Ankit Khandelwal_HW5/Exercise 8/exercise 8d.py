"""
Home Work 5
Ankit Khandelwal
Exercise 8d
15863
"""

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from time import perf_counter

start = perf_counter()

M = 1.989*10**30
vx = 0
vy = 15768000     
G = 6.6375*10**-5
x0 = 4*10**9
y0 = 0
delta = 1

def f(solution):
    x = solution[0]
    y = solution[1]
    r = sqrt(x**2 + y**2)
    x1 = solution[2]
    y1 = solution[3]
    fx = x1
    fy = y1
    fx1 = -G*M*x/r**3
    fy1 = -G*M*y/r**3
    return np.array([fx, fy, fx1, fy1])

ti = 0
tf = 48
h = 1
hh=[]
solution = np.array([x0, y0, vx, vy], float) 

xpoints = []
ypoints = []
xpoints.append(solution[0])
ypoints.append(solution[1])
x_points = []
y_points = []

check = np.array([x0, y0, vx, vy], float) 
x_points.append(check[0])
y_points.append(check[1])
final = np.array([x0, y0, vx, vy], float)

while ti < tf:
    check_h = 0
    while check_h == 0:
        for t in [ti, ti+h]:
            k1 = h*f(solution)
            k2 = h*f(solution+0.5*k1) 
            k3 = h*f(solution+0.5*k2) 
            k4 = h*f(solution+k3)
            solution += (k1 + 2*k2 + 2*k3 + k4 )/6 
            xpoints.append(solution[0])
            ypoints.append(solution[1])
        
        h=2*h
        for t in [ti]:
            k1 = h*f(check)
            k2 = h*f(check+0.5*k1) 
            k3 = h*f(check+0.5*k2) 
            k4 = h*f(check+k3)
            check += (k1 + 2*k2 + 2*k3 + k4 )/6
            x_points.append(check[0])
            y_points.append(check[1])
        
        h = h/2
        e1 = 1./30 * (xpoints[-1] - x_points[-1])
        e2 = 1./30 * (ypoints[-1] - y_points[-1])
        error = sqrt(e1**2 + e2**2)
        if error == 0:
            h_new = 1.5*h
        else:
            h_new = h * (h*delta / error)**(1/4)
        if h_new > 1.5*h:
            h_new = 1.5*h
        if h_new < h:
            h = h_new
            solution = final.copy()
            check = final.copy()
            xpoints.pop(-1)
            ypoints.pop(-1)
            xpoints.pop(-1)
            ypoints.pop(-1)
        else:
            ti = ti + 2*h
            check_h = 1
            final = solution.copy()
            check = solution.copy()
            h = h_new
    
    hh.append(h)

plt.plot(xpoints, ypoints, 'b.', markersize=1)
plt.xlabel('X in km')
plt.ylabel('Y in km')
plt.title('Trajectory')
plt.show()

end = perf_counter()
print('Time taken = {} seconds for 1 orbit.'.format((end-start)))
