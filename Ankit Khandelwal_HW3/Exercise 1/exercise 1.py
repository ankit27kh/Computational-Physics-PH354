"""
Ankit Khandelwal
15863
Exercise 1
"""

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

x = input('Enter a number: ')
print('\nFactorial of int(',x,') is :',factorial(int(x)))
print('\nFactorial of float(',x,') is :',factorial(float(x)))
