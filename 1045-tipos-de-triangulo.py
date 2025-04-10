a,b,c = input().split()
a,b,c = float(a),float(b),float(c)

#ordem decrescente
if(a<b):
    troca = a
    a = b
    b = troca
if(b<c):
    troca = b
    b = c
    c = troca   
if(a<b):
    troca = a
    a = b
    b = troca 
#tipo triangulo
if(a>=b+c):
    print('NAO FORMA TRIANGULO')
elif(a**2)==(b**2)+(c**2):
    print('TRIANGULO RETANGULO')
elif((a**2)>(b**2)+(c**2)):
    print('TRIANGULO OBTUSANGULO')
elif (a**2)<(b**2)+(c**2):
    print('TRIANGULO ACUTANGULO')
# equilatero ou isosceles
if(a==b==c):
    print('TRIANGULO EQUILATERO')
elif(a==b or b==c or c==a):
    print('TRIANGULO ISOSCELES')