# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

qts_pares = [a,b,c,d,e]
cont = 0

for valor in qts_pares:
    if valor % 2 == 0:
        cont += 1

print(f"{cont} valores pares")