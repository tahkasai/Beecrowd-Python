C = int(input())
T = input()

matriz = []

if (0<=C and C<=11):
    for i in range (12):
        lista = []
        for j in range (12):
            numero = float(input())
            lista.append(numero)
        matriz.append(lista)

    resultado = 0
    
    for k in range (len(matriz)):
        resultado += matriz[k][C]
    if T=='M':
        resultado /= 12
    
    print(f'{resultado:.1f}')