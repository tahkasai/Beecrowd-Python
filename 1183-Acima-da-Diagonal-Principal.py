O = input()

diagonal = []

for i in range (3):
    lista = []
    for j in range(3): 
        numero = float(input())
        lista.append(numero)
    diagonal.append(lista)

resultado = 0
contador = 0

for linha in range (len(diagonal)):
    for coluna in range (len(diagonal)):
        coluna = 0
        colunas = coluna + 1
        resultado += diagonal[linha][colunas]

if O =="M":
    resultado/= contador

print(f'{resultado:.1f}')