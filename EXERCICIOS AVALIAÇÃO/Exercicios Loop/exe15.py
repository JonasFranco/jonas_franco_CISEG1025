contador = 0

while contador <= 255:

    for i in range(20):
        if contador > 255:
            break
        print(f"{contador:3} -> {chr(contador)}")
        contador += 1

    opcao = input("Continuar? (sim ou nao): ").lower()
    if opcao != "sim":
        print("Termina programa")
        break

print("final.")
