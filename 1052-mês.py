# Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

# A entrada contém um único valor inteiro.

# Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

mes = int(input()) 

meses = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'} # Cria um dicionário chamado meses, onde cada número de 1 a 12 é uma chave (representando o mês) e o valor correspondente é o nome do mês em inglês.

if mes in meses.keys(): # Verifica se o número inserido pelo usuário (mes) está presente entre as chaves do dicionário meses. A função keys() retorna todas as chaves do dicionário.
    
    print(meses[mes]) # Caso o número inserido pelo usuário seja uma chave válida no dicionário, o programa imprime o valor correspondente, ou seja, o nome do mês em inglês.