palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

lista = palavras[:]

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        
        p1 = lista[j].lower()
        p2 = lista[j + 1].lower()
        
        if p1 < p2:   
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)