x = int(input())
y = int(input())
 
if (x > y):
    troca = x
    x = y
    y = troca
 
soma = 0
i = x + 1

while (i < y):
    if i % 2 == 1:
        soma += i
    i += 1
 
print(soma)