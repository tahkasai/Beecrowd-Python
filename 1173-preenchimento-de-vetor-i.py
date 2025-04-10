n = []
num = int(input())

n.append(num)  

for i in range(1, 10):
    num *= 2  
    n.append(num)

for i, j in enumerate(n):
    print(f'N[{i}] = {j}')