# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

cod1,peca1,valor1 = input().split()
cod1,peca1,valor1 = int(cod1),int(peca1),float(valor1)

cod2,peca2,valor2 = input().split()
cod2,peca2,valor2 = int(cod2),int(peca2),float(valor2)

print(f'VALOR A PAGAR: R$ {(peca1*valor1)+(peca2*valor2):.2f}')