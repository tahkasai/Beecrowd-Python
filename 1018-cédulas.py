cedula = int(input())

cem = cedula//100
cinquenta = (cedula - (cem*100))//50
vinte = (cedula - (cinquenta*50) - (cem*100))//20
dez = (cedula - (vinte*20) - (cinquenta*50) - (cem*100))//10
cinco = (cedula - (dez*10) - (vinte*20) - (cinquenta*50) - (cem*100))//5
dois = (cedula - (cinco*5)- (dez*10) - (vinte*20) - (cinquenta*50) - (cem*100))//2
um = (cedula - (dois*2)- (cinco*5)- (dez*10) - (vinte*20) - (cinquenta*50) - (cem*100))//1

print(cedula)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')