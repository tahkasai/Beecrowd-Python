from math import ceil, sqrt

def primo(x):
    if x % 2 == 0: return x == 2
    metade = x // 2
    for p in range(3, metade+1, 2):
        if x % p == 0:
            return False
    return True

n = int(input())

for i in range(n):
    x = int(input())
    if primo(x):
        print(f'Prime')
    else:
        print(f'Not Prime')