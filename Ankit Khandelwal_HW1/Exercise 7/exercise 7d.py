a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2
max_b=[]
index_b=[]
for Z in range(1,101):
    b=[]
    for A in range(Z,(3*Z)+1):
        if A%2 != 0:
            a5 = 0
        elif A%2 == 0 and Z%2 == 0:
            a5 = 12
        else:
            a5 = -12
        B = a1*A - a2*(A**(2/3)) - a3*(Z**2)/(A**(1/3)) - a4*((A-2*Z)**2)/A + a5/(A**(1/2))
        b.append(B/A)
    index = b.index(max(b))
    max_ = max(b)
    print('\nMax B/A value is for A =',Z+index, 'for Z =', Z)
    print('Max B/A is:',max_)
    max_b.append(max_)
    index_b.append(index+Z)
index1 = max_b.index(max(max_b))
max_1 = max(max_b)
print('\nOverall Max B/A is:', max(max_b))
print('Overall Max B/A is for Z =', index1+1, 'for A =', index_b[index1])
