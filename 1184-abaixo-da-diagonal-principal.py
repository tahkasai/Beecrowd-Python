O = input()

diagonal = []

for i in range (0,12):
    lista = []
    for j in range(0,12): 
        numero = float(input())
        lista.append(numero)
    diagonal.append(lista)

resultado = 0

for linha in range (len(diagonal)):
    for coluna in range (len(diagonal)):
        if (linha>coluna):
            resultado+= diagonal[linha][coluna]

if O =="M":
    resultado/= 66

print(f'{resultado:.1f}')