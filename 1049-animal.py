corpo = input()
tipo = input()
come = input()

if (corpo == "vertebrado"):
    if (tipo == "ave"):
        if (come == "carnivoro"):
            print ('aguia')
        elif(come == "onivoro"):
            print('pomba')
    elif (tipo == 'mamifero'):
        if (come == 'onivoro'):
            print('homem')
        elif(come == 'herbivoro'):
            print('vaca')
elif(corpo == 'invertebrado'):
    if (tipo == 'inseto'): 
        if(come == 'hematofago'):
            print('pulga')
        elif(come == 'herbivoro'):
            print('lagarta')       
    elif(tipo == 'anelideo'):
        if(come == 'hematofago'):
            print('sanguessuga')
        elif(come == 'onivoro'):
            print('minhoca')
