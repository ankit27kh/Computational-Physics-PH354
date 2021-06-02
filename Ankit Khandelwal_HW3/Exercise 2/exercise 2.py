"""
Ankit Khandelwal
15863
Exercise 2
"""

from math import sqrt

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

[x1, x2] = [(-b + sqrt(b ** 2 - 4 * a * c)) / 2 / a, (-b - sqrt(b ** 2 - 4 * a * c)) / 2 / a]

print('Solutions of ', a, 'x^2 +', b, 'x +', c, '= 0 is by first formula: ', [x1, x2])

[x11, x22] = [2 * c / (-b - sqrt(b ** 2 - 4 * a * c)), 2 * c / (-b + sqrt(b ** 2 - 4 * a * c))]

print('\nSolutions of ', a, 'x^2 +', b, 'x +', c, '= 0 by modified  formula is: ', [x11, x22], )

if b < 0:
    xA = 2 * c / (-b + sqrt(b ** 2 - 4 * a * c))
    xB = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 / a
else:
    xA = (-b - sqrt(b ** 2 - 4 * a * c)) / 2 / a
    xB = 2 * c / (-b - sqrt(b ** 2 - 4 * a * c))

print('\nSolutions of ', a, 'x^2 +', b, 'x +', c, '= 0 by modified general formula is: ', xA, xB)
