'''
ANKIT KHANDELWAL
15863

Exercise 8
'''

def binomial(n,k):
    def factorial(i):
        if i == 0:
            return 1
        else:
            return i*factorial(i-1)
    return int(factorial(n)/(factorial(k)*factorial(n-k)))

#8a    
N = int(input('Enter n: '))
K = int(input('Enter k: '))
print('The binomial coefficient is :',binomial(N,K), '\n')

#8b
l=20
print('Pascal\'s Trinagle\n')
for i in range(1,l+1):
    for j in range(0,i+1):
        print(binomial(i,j), end= ' ')
    print('')

#8c
n = 100
k = 60
prob = binomial(n, k)/2**n
print('\nThe probabiolity that 60 heads come in 100 throws is:',prob)
for i in range(61, 101):
    prob = prob + binomial(n, i)/2**n
print('\nThe probability that heads come 60 or more times is:', prob)
