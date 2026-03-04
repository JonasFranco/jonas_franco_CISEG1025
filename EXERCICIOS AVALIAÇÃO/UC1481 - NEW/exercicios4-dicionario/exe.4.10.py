frase = input("Introduza uma frase: ")
resultado = {}
palavra_acumulada = ""
it = 0

while it < len(frase):
    letra = frase[it]

    if letra != " ":
        palavra_acumulada = palavra_acumulada + letra

    if letra == " " or it == len(frase) - 1:
        if palavra_acumulada != "":
            if palavra_acumulada in resultado:
                resultado[palavra_acumulada] = resultado[palavra_acumulada] + 1
            else:
                resultado[palavra_acumulada] = 1
            palavra_acumulada = "" 
            
    it += 1

print(resultado)