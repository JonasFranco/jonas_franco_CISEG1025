nome = input("Introduza o seu nome completo: ")
 
valido = True
comprimento = len(nome)
 
for i in range(comprimento):
    char = nome[i]
    ascii_code = ord(char)
    if ascii_code == 32:
        if i + 1 < comprimento:
            proximo_ascii = ord(nome[i + 1])
            if not (65 <= proximo_ascii <= 90):
                valido = False
                break
        continue
    elif 97 <= ascii_code <= 122:
        if i == 0 or ord(nome[i - 1]) == 32:
            valido = False
            break
    elif 65 <= ascii_code <= 90:
        if i != 0 and ord(nome[i - 1]) != 32:
            valido = False
            break
    else:
        valido = False
        break
 
if valido:
    print("Nome válido!")
else:
    print("Nome inválido: contém caracteres não permitidos.")