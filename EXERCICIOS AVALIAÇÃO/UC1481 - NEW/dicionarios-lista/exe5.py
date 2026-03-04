def contar_letras():
    palavra = input("Digite uma palavra: ")
    resultado = {}

    for letra in palavra:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1

    print(resultado)

contar_letras()