num = int(input())
resultado = num

if (0<num<13):
    i = 1
    while(i<num):
        resultado = resultado * (num-i)
        i+=1
print(f'{resultado*1}')
