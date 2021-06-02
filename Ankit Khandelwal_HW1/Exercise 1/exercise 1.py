'''
ANKIT KHANDELWAL
15863

Exercise 1
'''

import math


def altitude(T):
    R_Earth = 6378100
    g_Earth = 9.803
    R_sat = ((T * R_Earth * math.sqrt(g_Earth)) / 2 / math.pi) ** (2 / 3)
    return R_sat - R_Earth


# 1a
T = int(input('Enter period of rotation in seconds: '))
print('The altitude of satellite above Earth\'s surface is:', altitude(T), 'meters.\n')

# 1b
print('The altitude of satellite above Earth\'s surface is:', altitude(90 * 60),
      'meters for orbit period of 90 minutes.\n')
print('The altitude of satellite above Earth\'s surface is:', altitude(45 * 60),
      'meters for orbit period of 45 minutes.\n')
print('The altitude of satellite above Earth\'s surface is:', altitude(1 * 24 * 60 * 60),
      'meters for orbit period of 1 day.\n')
'''
The result shows that we can not have an orbit period of 45 minutes.
'''

# 1c
print('The altitude of satellite above Earth\'s surface is:', altitude(24 * 60 * 60),
      'meters for orbit period of 24 hours.\n')
print('The altitude of satellite above Earth\'s surface is:', altitude(23.93 * 60 * 60),
      'meters for orbit period of 23.93 hours.\n')
print('The difference between the two is:', altitude(24 * 60 * 60) - altitude(23.93 * 60 * 60),
      'meters.\n')
'''
Earth does not take complete 24 hours for one rotation around its axis.
Thus if we use 24 days, the satellite will not remain geosynchronous.
'''
