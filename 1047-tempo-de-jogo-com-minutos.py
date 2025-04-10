hi, mi, hf, mf = map(int,input().split())

# Cálculo das horas
if hi == hf and mi == mf:
    hora = 24
    minutos = 0
else:
    if hf > hi or (hf == hi and mf >= mi):
        hora = hf - hi
    else:
        hora = 24 - hi + hf

# Cálculo dos minutos
if mf >= mi:
    minutos = mf - mi
else:
    minutos = (60 - mi) + mf
    hora -= 1

print(f'O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)')