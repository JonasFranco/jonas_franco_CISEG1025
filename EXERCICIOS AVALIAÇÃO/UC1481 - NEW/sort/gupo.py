palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

grupos = {}

for palavra in palavras:
    inicial = palavra[0]
    
    if inicial not in grupos:
        grupos[inicial] = []
    
    grupos[inicial].append(palavra)

for chave in grupos:
    lista = grupos[chave]
    
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(grupos)