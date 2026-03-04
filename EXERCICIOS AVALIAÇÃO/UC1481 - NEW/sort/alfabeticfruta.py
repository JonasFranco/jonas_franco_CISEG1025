palavras = ["banana", "uva", "abacaxi", "laranja"]

lista = palavras[:]

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        
        palavra1 = lista[j]
        palavra2 = lista[j + 1]
        
        trocar = False
        
        for k in range(min(len(palavra1), len(palavra2))):
            if ord(palavra1[k]) > ord(palavra2[k]):
                trocar = True
                break
            elif ord(palavra1[k]) < ord(palavra2[k]):
                break
            
        if not trocar and palavra1.startswith(palavra2) and len(palavra1) > len(palavra2):
            trocar = True
        
        if trocar:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)