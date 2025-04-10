cod,quant = input().split()
cod,quant = int(cod),int(quant)

lanche = {1:4.0,2:4.5,3:5,4:2,5:1.5}

print (f'Total: R$ {(lanche[cod]*quant):.2f}')
