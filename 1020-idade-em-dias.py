num = int(input())

ano = num // 365
mes = (num%365)//30
dia = (num%365)%30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')