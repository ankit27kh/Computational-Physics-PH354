"""
Ankit Khandelwal
15863
Exercise 11
"""


def f(x, y):
    return y ** 2 * (1 - x) - x ** 3


def g(x, y):
    return y ** 2 + x ** 2 - 1


def fderx(x, y):
    return -y ** 2 - 3 * x ** 2


def fdery(x, y):
    return 2 * y - 2 * y * x


def gderx(x):
    return 2 * x


def gdery(y):
    return 2 * y


x = 1
y = 1
print('Root 1')
while abs(f(x, y)) > 10 ** -10 or abs(g(x, y)) > 10 ** -10:
    print(x, y)
    y = y + (gderx(x) * f(x, y) - fderx(x, y) * g(x, y)) / (fderx(x, y) * gdery(y) - fdery(x, y) * gderx(x))
    x = x + (fdery(x, y) * g(x, y) - gdery(y) * f(x, y)) / (fderx(x, y) * gdery(y) - fdery(x, y) * gderx(x))
print(x, y)

x = 1
y = -1
print('\nRoot 2')
while abs(f(x, y)) > 10 ** -10 or abs(g(x, y)) > 10 ** -10:
    print(x, y)
    y = y + (gderx(x) * f(x, y) - fderx(x, y) * g(x, y)) / (fderx(x, y) * gdery(y) - fdery(x, y) * gderx(x))
    x = x + (fdery(x, y) * g(x, y) - gdery(y) * f(x, y)) / (fderx(x, y) * gdery(y) - fdery(x, y) * gderx(x))
print(x, y)
