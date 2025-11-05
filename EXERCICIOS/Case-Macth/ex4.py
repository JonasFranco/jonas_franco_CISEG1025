valor = input("Digite um valor: ")

try:
    int(valor)
    print("Número inteiro")
except:
    try:
        float(valor)
        print("Número decimal")
    except:
        match valor:
            case _ if valor.startswith("[") and valor.endswith("]"):
                print("Lista")
            case _ if valor.isnumeric():
                print("String numérica")
            case _ if valor.isalpha() or " " in valor:
                print("String textual")
            case _:
                print("Tipo desconhecido")
