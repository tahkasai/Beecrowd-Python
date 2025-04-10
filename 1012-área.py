# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

# O arquivo de entrada contém três valores com um dígito após o ponto decimal.

# O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

A,B,C = input().split() #o split() basicamente separa cada variavél quando há um espaço
A,B,C = float(A),float(B),float(C) #aqui é pra definir que tipo de variavél é 

print (f'TRIANGULO: {A * C / 2 :.3f}') 
print (f'CIRCULO: {3.14159 * C ** 2 :.3f}') 
print (f'TRAPEZIO: {(A + B) * C / 2 :.3f}') 
print (f'QUADRADO: {B ** 2 :.3f}') 
print (f'RETANGULO: {A * B :.3f}') 