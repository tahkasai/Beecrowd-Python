tabela = []

canais = int(input())

if 1 <= canais and canais<=200:
    for i in range (canais):
        nome,inscritos,monetizacao,simOuNao = input().split(";")
        inscritos,monetizacao = int(inscritos),float(monetizacao)

        tabela.append((nome,inscritos,monetizacao,simOuNao))
        #1-string, 2- int, 3- double, 4- string

    #valor que eles vão receber a cara 1000 inscritos
    x = float(input()) # canais premium
    y = float(input()) # canais não premium

    def imprimir_saida(nome,inscritos,monetização,simOuNao):
        if simOuNao.lower() == "sim":
            Valor = x
        else:
            Valor = y

        Valor_Inscritos = (inscritos // 1000) * Valor
        total = Valor_Inscritos + monetização
        print(f'{nome}: R$ {total:.2f}')

    print("-----")
    print("BÔNUS")
    print("-----")
    for canal in tabela:
        nome,inscritos,monetizacao,simOuNao = canal
        imprimir_saida(nome,inscritos,monetizacao,simOuNao)