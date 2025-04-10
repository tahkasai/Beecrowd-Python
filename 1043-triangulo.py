a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

# primeira verificação
if a < b:
    menor1 = a
    menor2 = b
else: 
    menor1 = b
    menor2 = a

# Segunda verificação
if menor2 < c:
    maior = c
elif menor2 > c:
    maior = menor2
    menor2 = c
else:
    maior = menor2  # Definindo `maior` no caso de igualdade

# terceira verificação
if menor2 < menor1:
   troca = menor1
   menor1 = menor2
   menor2 = troca

# Perimetro ou Area
if (menor1 + menor2) > maior:
    print(f'Perimetro = {(a + b + c):.1f}')
else:
    print(f'Area = {(((a + b) * c) / 2):.1f}')
