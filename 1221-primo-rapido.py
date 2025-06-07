from math import *

def primo(x):
    if x % 2 == 0:
        return x == 2
    raiz = ceil(sqrt(x))
    for i in range (3,raiz+1,2):
        if x % i == 0:
            return False
        return True
    

num = int(input())
lista = []
i=1
while i<=num:
    x = int(input())
    if primo(x) == True:
        lista.append("Prime")
    else:
        lista.append("Not Prime")
    i+=1

for t in lista:
    print(t)


    