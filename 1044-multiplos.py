#Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

#A entrada contém valores inteiros.

#A saída deve conter uma das mensagens conforme descrito acima.

A, B = input().split()
A, B = int(A),int(B)

if (A % B == 0) or (B % A == 0) :
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')