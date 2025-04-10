inicial,final = map(int,input().split())

if(inicial==final):
    print("O JOGO DUROU 24 HORA(S)")
elif(inicial<final):
    print(f'O JOGO DUROU {final-inicial} HORA(S)')
else:
    print(f'O JOGO DUROU {(24-inicial)+final} HORA(S)')
