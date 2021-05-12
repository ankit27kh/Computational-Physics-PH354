from math import *
import matplotlib.pyplot as plt

def simpsons_rule (fx, a, b):
    c = (a+b) / 2.0
    h = abs(b-a) / 6.0
    return h *(fx(a) + 4.0* fx(c) + fx(b))
def recursive_asr (fx, a, b, eps, whole):
    c = (a+b) / 2.0
    left = simpsons_rule (fx, a, c)
    right = simpsons_rule (fx, c, b)
    if abs( left + right - whole ) <= 15* eps:
        return left + right + ( left + right - whole )/15.0
    return recursive_asr (fx, a, c, eps /2.0 , left ) +  recursive_asr (fx, c, b, eps /2.0 , right )
def adaptive_simpsons_rule (fx, a, b, eps ):
    return recursive_asr (fx, a, b, eps , simpsons_rule (fx, a, b))
def gamma(a0):
    def fx(x):
        c = a0-1
        if x == 0 or x == 1:
            return 0
        else:
            return exp(((a0-1)*log(x*c/(1-x))) - (x*c/(1-x))) * c/(1-x)**2
    return adaptive_simpsons_rule(fx ,0 ,1 ,10**-10)

print(gamma(3/2),'gamma(3/2)')
print(gamma(3),'gamma(3)')
print(gamma(6),'gamma(6)')
print(gamma(10),'gamma(10)')