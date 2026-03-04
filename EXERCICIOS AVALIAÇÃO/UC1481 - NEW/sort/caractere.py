palavra = "algoritmo"

letras = list(palavra)

for i in range(len(letras)):
    for j in range(len(letras) - 1):
        if ord(letras[j]) > ord(letras[j + 1]):
            letras[j], letras[j + 1] = letras[j + 1], letras[j]

resultado = "".join(letras)

print(resultado)