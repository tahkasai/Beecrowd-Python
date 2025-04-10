num = float(input())

p1 = int(num)
p2 = int((num-p1)*100)

if (0 <= num <= 1000000.00):
    n100 = p1//100
    n50 = (p1%100)//50
    n20 = ((p1%100)%50)//20
    n10 = (((p1%100)%50)%20)//10
    n5 = ((((p1%100)%50)%20)%10)//5
    n2 = (((((p1%100)%50)%20)%10)%5)//2

    print('NOTAS:')
    print(f'{n100:.0f} nota(s) de R$ 100.00')
    print(f'{n50:.0f} nota(s) de R$ 50.00')
    print(f'{n20:.0f} nota(s) de R$ 20.00')
    print(f'{n10:.0f} nota(s) de R$ 10.00')
    print(f'{n5:.0f} nota(s) de R$ 5.00')
    print(f'{n2:.0f} nota(s) de R$ 2.00')

    m1 = ((((((p1%100)%50)%20)%10)%5)%2)//1
    m50 = (p2%100)//50
    m25 = ((p2%100)%50)//25
    m10 = (((p2%100)%50)%25)//10
    m05 = ((((p2%100)%50)%25)%10)//5
    m01 = (((((p2%100)%50)%25)%10)%5)//1

    print('MOEDAS:')
    print(f'{m1:.0f} moeda(s) de R$ 1.00')
    print(f'{m50:.0f} moeda(s) de R$ 0.50')
    print(f'{m25:.0f} moeda(s) de R$ 0.25')
    print(f'{m10:.0f} moeda(s) de R$ 0.10')
    print(f'{m05:.0f} moeda(s) de R$ 0.05')
    print(f'{m01:.0f} moeda(s) de R$ 0.01')