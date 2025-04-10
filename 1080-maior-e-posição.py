i = 1
maior = 0
posicao = 0
while(i<=100):
    num = int(input())
    if(maior<num):
        maior=num
        posicao = i
    i+=1
    
print(maior)
print(posicao)