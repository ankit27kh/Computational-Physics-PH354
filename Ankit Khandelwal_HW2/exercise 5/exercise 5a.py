from numpy import sqrt, pi, exp, linspace, zeros
from math import factorial
import matplotlib.pylab as plt

from numpy import ones,copy,cos,tan,pi,linspace

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

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

def H(n, x):
    def H_iter(a, b, count):
        if count == 0:
            return b
        else:
            return H_iter(2 * x * a - 2 * (count - 1) * b, a, count-1)
    return H_iter(2 * x, 1, n)

def wave_func(n, x):
    return (1 / (sqrt((2**n)*factorial(n)*sqrt(pi)))) * exp(-0.5*(x**2)) * H(n, x)
N = 200
d = linspace(-4, 4, N)
y = zeros([N, 4], float)
for j in range(0, 4, 1):
    for i in range(0, N, 1):
        y[i, j] = wave_func(j, d[i])
y2 = []
d2 = linspace(-10, 10, 500)
for m in range(0, 500, 1):
    y2.append(wave_func(30, d2[m]))
f1 = plt.figure(1)
plt.plot(d2, y2, 'b-', label=r"$\psi_{30}$", linewidth=1)
plt.xlabel("x")
plt.ylabel(r"$\psi(x)$")
f2 = plt.figure(2)
plt.plot(d, y[:, 0], label=r"$\psi_0$")
plt.plot(d, y[:, 1], label=r"$\psi_1$")
plt.plot(d, y[:, 2], label=r"$\psi_2$")
plt.plot(d, y[:, 3], label=r"$\psi_3$")
plt.xlabel("x")
plt.ylabel(r"$\psi(x)$")
plt.show()
