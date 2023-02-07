# dice

import random

d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

for x in range(0, 100000):
    print('choose you dice size. d20 or d12')
    size = input()
    if size == 'd12':
        print(' ')
        print(random.choice(d12))
    elif size == 'd20':
        print(' ')
        print(random.choice(d20))
    else:
        print(' ')
        print('pleas input a valid dice size')