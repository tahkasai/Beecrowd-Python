x = []
for i in range(10):
    num = int(input())
    if num < 0 or num == 0:
        x.append(1)  # Se o número for negativo ou 0, adiciona 1 na lista
    else:
        x.append(num)  # Caso contrário, adiciona o próprio número

# Aqui usamos enumerate para acessar o índice e o valor dos elementos da lista
for i, j in enumerate(x):
    print(f'X[{i}] = {j}')