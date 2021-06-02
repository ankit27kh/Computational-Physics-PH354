import matplotlib.pylab as plt
from numpy import sqrt, sin, cos, pi, linspace, zeros


def q(u, alpha):
    return sin(alpha * u) ** 2


def i_n(x):
    l = 500e-9
    d = 20e-6
    w = 10 * d
    alpha = pi / d
    a = -1 * w / 2
    b = w / 2
    N = 20
    h = d / 2
    sum1 = sqrt(q(a, alpha)) * cos((2 * pi * x * a) / l) + sqrt(q(b, alpha)) * cos((2 * pi * x * b) / l)
    for k in range(1, N, 2):
        sum1 = sum1 + 4 * (sqrt(q((a + (k * h)), alpha)) * cos((2 * pi * x * (a + (k * h)) / l)))
    for k in range(2, N, 2):
        sum1 = sum1 + 2 * (sqrt(q((a + (k * h)), alpha)) * cos((2 * pi * x * (a + (k * h)) / l)))
    i_cos = (h / 3) * sum1
    sum2 = sqrt(q(a, alpha)) * sin((2 * pi * x * a) / l) + sqrt(q(b, alpha)) * sin((2 * pi * x * b) / l)
    for k in range(1, N, 2):
        sum2 = sum2 + 4 * (sqrt(q((a + (k * h)), alpha)) * sin((2 * pi * x * (a + (k * h)) / l)))
    for k in range(2, N, 2):
        sum2 = sum2 + 2 * (sqrt(q((a + (k * h)), alpha)) * sin((2 * pi * x * (a + (k * h)) / l)))
    i_sin = (h / 3) * sum2
    return (i_cos ** 2) + (i_sin ** 2)


n = 1000
p = linspace(-5, 5, n)
intensity = []
D = zeros([50, 1000], float)
for j in range(n):
    c = i_n(1e-2 * p[j])
    intensity.append(c)
    for k in range(0, 50, 1):
        D[k, j] = c

f1 = plt.figure(1)
plt.plot(p, intensity)

f2 = plt.figure(2)
plt.imshow(D, vmax=0.25e-08, extent=[-5, 5, 0, 2])
plt.hot()
plt.show()
