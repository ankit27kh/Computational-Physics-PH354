'''
ANKIT KHANDELWAL
15863

Exercise 2
'''

import math

def polar(x,y):
    r = math.sqrt(x**2+y**2)
    if x == 0:
        if y > 0:
            theta_degrees = 90
        elif y == 0:
            theta_degrees = 0
        else:
            theta_degrees = 270
    else:
        theta = math.atan(abs(y/x))
        theta_degrees = math.degrees(theta)
    if y>=0 and x>0:
        theta_degrees = theta_degrees
    elif y>0 and x<0:
        theta_degrees = theta_degrees+90
    elif y<=0 and x<0:
        theta_degrees = theta_degrees+180
    elif y<0 and x>0:
        theta_degrees = theta_degrees+270
    return(r,theta_degrees)
    
x=int(input('Enter X cordinate: '))
y=int(input('Enter Y cordinate: '))
(r,theta_degrees) = polar(x,y)
print('\nThe point in polar cordinates is: (',r,',',theta_degrees,')')
