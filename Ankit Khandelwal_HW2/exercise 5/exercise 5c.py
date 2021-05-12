from numpy import sqrt, pi, exp
from math import factorial
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


def wave_func(n, z):
    p = z / (1 - (z**2))
    return ((1+(z**2))/((1-(z**2))**2)) * (p**2) * (((1 / (sqrt((2**n)*factorial(n)*sqrt(pi)))) * exp(-0.5*(p**2)) * H(n, p)) ** 2)


n = int(input("Enter the order of the wave function: "))
N = 100
a = -1.0
b = 1.0
x, w = gaussxw(N)
xp = 0.5 * (b - a) * x + 0.5 * (b + a)
wp = 0.5 * (b - a) * w
s = 0.0
for k in range(N):
    s += wp[k] * wave_func(n, xp[k])

print("Uncertainty for the ", n, "th order state:", sqrt(s))
