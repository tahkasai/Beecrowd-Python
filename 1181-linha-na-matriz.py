L = int(input()) # número da linha

# criação da matriz
matriz = []

if (0<=L and L<=2):
    T = input() # tipo da operação

    for i in range(12):
        linha = []
        for j in range(12):
            numero = int(input())
            linha.append(numero)
        matriz.append(linha)

    # zerando variavel
    resultado = 0

    # Operação
    if T == "S":
        for k in range(len(matriz)):
            resultado += matriz[L][k]
    elif T == "M":
        for k in range(len(matriz)):
            resultado += matriz[L][k]
        resultado /= 12

# exibir
print(f'{resultado:.1f}')
