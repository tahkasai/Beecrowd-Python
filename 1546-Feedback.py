dicionario = {1:'Rolien',2:'Naej',3:'Elehcim',4:'Odranoel'}

n = int(input('')) # número de dias trabalhados

i = 1
while i<=n:
    k = int(input('')) # número de feedbacks no dia
    ik = 1
    while ik<=k:
        feedback = int(input('')) # número do feedback
        print (dicionario[feedback])
        ik+=1
    i+=1