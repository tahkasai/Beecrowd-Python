noivo = []
noiva = []

while True:
    entrada = input()
    if entrada == "ACABOU":
        break
    nome, convidadeQuem = entrada.split(';')
    
    if convidadeQuem == "noivo":
        noivo.append(nome)
    elif convidadeQuem == "noiva":
        noiva.append(nome)

def imprimir_lista(titulo,lista):
    print("--------------------")
    print(titulo)
    print("--------------------")
    if lista:
        print("\n".join(lista))

lista_final = sorted(set(noiva) | set(noivo))  
apenas_noiva = sorted(set(noiva)-set(noivo))
apenas_noivo = sorted(set(noivo)-set(noiva))
por_ambos = sorted(set(noiva) & set(noivo))
um_deles = sorted((set(noiva) | set(noivo)) - (set(noiva) & set(noivo)))

imprimir_lista("LISTA FINAL",lista_final)
print("*")
imprimir_lista("APENAS NOIVA",apenas_noiva)
print("*")
imprimir_lista("APENAS NOIVO", apenas_noivo)
print("*")
imprimir_lista("POR AMBOS", por_ambos)
print("*")
imprimir_lista("POR APENAS UM DELES", um_deles)
