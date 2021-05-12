from numpy import *
import matplotlib.pyplot as plt

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def f1(n, y, z):
    return 1/sqrt(((n**2)+(y**2)+(z**2)) ** 3)

def f2(y, z, x, w):
    a = -5
    b = 5
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w
    s2 = 0.0
    for k in range(N):
        s2 += wp[k] * f1(xp[k], y, z)
    return s2

def f3(z, x, w):
    a = -5
    b = 5
    yp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w
    s1 = 0.0
    for k in range(N):
        s1 += wp[k] * f2(yp[k], z, x, w)
    return s1

N = 100
d1 = linspace(0, 0.3, 100)
x, w = gaussxw(N)
force1 = []
for k in range(0, 100, 1):
    force1.append(6.674e-9 * d1[k] * f3(d1[k], x, w))
d2 = linspace(0.3, 10, 50)
force2 = []
for k in range(0, 50, 1):
    force2.append(6.674e-9 * d2[k] * f3(d2[k], x, w))

plt.plot(d1, force1, 'r.')
plt.plot(d2, force2, 'b.')
plt.xlabel("Distance from centre(m)")
plt.ylabel("Force(N)")
plt.show()
