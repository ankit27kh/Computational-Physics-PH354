from numpy import sqrt, sin, cos, pi, linspace, zeros
import matplotlib.pylab as plt

def i_n(x, a, b):
    l = 500e-9
    N = 20
    h = (b - a) / N
    sum1 = cos((2*pi*x*a)/l) + cos((2*pi*x*b)/l)
    for k in range(1, N, 2):
        sum1 = sum1 + 4 * (cos((2*pi*x*(a+(k*h))/l)))
    for k in range(2, N, 2):
        sum1 = sum1 + 2 * (cos((2 * pi * x * (a + (k * h)) / l)))
    i_cos = (h / 3) * sum1
    sum2 = sin((2 * pi * x * a) / l) + sin((2 * pi * x * b) / l)
    for k in range(1, N, 2):
        sum2 = sum2 + 4 * (sin((2 * pi * x * (a + (k * h)) / l)))
    for k in range(2, N, 2):
        sum2 = sum2 + 2 * ( sin((2 * pi * x * (a + (k * h)) / l)))
    i_sin = (h / 3) * sum2
    return i_cos, i_sin

n = 1000
p = linspace(-5, 5, n)
intensity = []
D = zeros([50, 1000], float)
d1 = 10e-6
d2 = 20e-6
w = 60e-6
a1 = (-1*w/2) - d1
b1 = (-1*w/2)
a2 = (w/2)
b2 = (w/2) + d2
for j in range(n):
    c1, s1 = i_n(1e-2 * p[j], a1, b1)
    c2, s2 = i_n(1e-2 * p[j], a2, b2)
    c = ((c1 + c2)**2) + ((s1 + s2)**2)
    intensity.append(c)
    for k in range(0, 50, 1):
        D[k, j] = c

plt.imshow(D, vmax=2.5e-10, extent=[-5, 5, 0, 2])
plt.hot()
plt.show()
