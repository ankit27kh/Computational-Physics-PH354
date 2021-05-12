"""
Ankit Khandelwal
15863
Exercise 5b
"""

def fy(x):
    a = 1
    b = 2
    return b/(a+x**2)

def fx(x, y):
    a = 1
    return y*(a + x**2)

x = 1
while abs(x - fx(x, fy(x))) > 10**-7:
    print(x, fy(x))
    x = fx(x, fy(x))
print('\nX value is:', x, 'Y value is:', fy(x))

# We can see that the solutiion is converging in just a single step
# after the guess.
# So what's asked in part b and part c is not clear.
# The solution is agreeing with part a exactly.
