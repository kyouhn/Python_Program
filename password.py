import time
from itertools import product

target = 'yufh'
chars = 'abcdefghijklmnopqrstuvwxyz'


def check(chars, repeat):
    pws = product(chars, repeat=repeat)

    for pw in pws:
        if ''.join(pw) == target:
            return ''.join(pw)


start = time.time()
pw = check(chars, 4)

if (pw is None):
    print('failure')
else:
    print('got it! -->', pw)

finish = time.time() - start
print(finish, ' sec');