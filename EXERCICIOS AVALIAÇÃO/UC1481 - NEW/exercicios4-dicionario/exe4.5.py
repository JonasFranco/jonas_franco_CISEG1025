palavra = input("Introduza uma palavra: ")
contagem = {}
it = 0

while it < len(palavra):
    letra = palavra[it]
    if letra in contagem:
        contagem[letra] = contagem[letra] + 1
    else:
        contagem[letra] = 1
    it += 1

print(contagem)