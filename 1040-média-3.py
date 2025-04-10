n1,n2,n3,n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print(f'Media: {media:.1f}')

if (media >= 7.0):
    print ("Aluno aprovado.")
    
elif (6.9 >= media >= 5.0):

    print ("Aluno em exame.")

    notaexame = float(input())
    mediafinal = (notaexame + media)/2

    print(f'Nota do exame: {notaexame:.1f}')
    if(mediafinal >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f'Media final: {mediafinal:.1f}')

else:
    print ("Aluno reprovado.")