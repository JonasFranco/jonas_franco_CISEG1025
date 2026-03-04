palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

lista = palavras[:]

def contar_minusculas(palavra):
    contador = 0
    for letra in palavra:
        if 'a' <= letra <= 'z':
            contador += 1
    return contador

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        
        if contar_minusculas(lista[j]) > contar_minusculas(lista[j + 1]):
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)