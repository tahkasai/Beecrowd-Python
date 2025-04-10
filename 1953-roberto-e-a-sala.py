while True: # EOF ou Fim de arquivo
    try:
        dicionario = {}

        n = int(input()) # número de alunos na sala

        for i in range(n):
            matricula,turma = input().split()
            dicionario[int(matricula)] = turma

        epr = ehd = intruso = 0

        for sala in dicionario.values():
            if sala == 'EPR':
                epr += 1
            elif sala == 'EHD':
                ehd += 1
            else:
                intruso += 1

        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intruso}')

    except EOFError:
        break
