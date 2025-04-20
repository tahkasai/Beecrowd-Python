porcentagem = reajuste = 0

salario = float(input())

if salario<=400:
    reajuste = 0.15 * salario
    porcentagem = 15
elif 400<salario and salario<=800:
    reajuste = 0.12 * salario
    porcentagem = 12
elif 800<salario and salario<=1200:
    reajuste = 0.1 * salario
    porcentagem = 10
elif 1200<salario and salario<=2000:
    reajuste= 0.07 * salario
    porcentagem = 7
elif salario>2000:
    reajuste= 0.04 * salario
    porcentagem = 4

novoSalario = salario+reajuste

print(f'Novo salario: {novoSalario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {porcentagem} %')