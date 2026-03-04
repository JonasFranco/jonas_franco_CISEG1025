def contar_palavras():
    frase = input("Digite uma frase: ")
    palavras = frase.split()
    resultado = {}

    for palavra in palavras:
        if palavra in resultado:
            resultado[palavra] += 1
        else:
            resultado[palavra] = 1

    print(resultado)

contar_palavras()