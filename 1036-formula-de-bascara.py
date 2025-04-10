import math

a,b,c = input().split()
a,b,c = float(a),float(b),float(c)

if(a!=0 and b!=0 and c!=0):
    delta = (b*b)-(4*a*c)
    if(delta<0):
        print('Impossivel calcular')
    else:
        raiz = math.sqrt(delta)

        r1 = (-b + raiz)/(2*a)
        r2 = (-b - raiz)/(2*a)

        print(f'R1 = {r1:.5f}')
        print(f'R2 = {r2:.5f}')
else:
    print('Impossivel calcular')