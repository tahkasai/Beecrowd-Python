num = int(input()) #tempo em segundos

print(f'{(num//3600)}:{((num//60)%60):.0f}:{num%60}') # na operação de minutos primeiro, o código calcula quantos minutos cabem no total de segundos (num // 60). O operador % 60 é usado para obter o valor dos minutos restantes, ignorando as horas já calculadas.