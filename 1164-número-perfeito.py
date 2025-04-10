n = int(input())  

if 1 <= n <= 20:
    for i in range(n):
        x = int(input())
        if 1 <= x <= 10**8:
            soma_divisores = 0
            for i in range(1, x // 2 + 1):  
                if x % i == 0:
                    soma_divisores += i
            
            if soma_divisores == x:
                print(f"{x} eh perfeito")
            else:
                print(f"{x} nao eh perfeito")
