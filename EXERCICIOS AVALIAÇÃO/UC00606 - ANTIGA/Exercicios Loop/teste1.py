opcao = 0

while opcao != 4:
    print("1 - Analisa números ")
    print("2 - Calculadora ")
    print("3 - Tabuada")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

# =======================================================================
    
    if opcao == 1:
        valor = int(input("Introduza um número entre 1 e 30000: "))

        while valor < 1 or valor > 30000:
            valor = int(input("Valor inválido! Introduza entre 1 e 30000: "))

        contador = valor

        pausa = 0  

        while contador >= 1:
            num = contador
            divisores = []
            for d in range(1, num + 1):
                if num % d == 0:
                    divisores.append(d)

            if len(divisores) == 2:
                primo = "É PRIMO"
            else:
                primo = "NÃO é primo"

            soma_div = 0
            for div in divisores:
                if div != num:
                    soma_div += div

            if soma_div == num:
                perfeito = "perfeito"
            else:
                perfeito = "n perfeito"

            print(f"\nNúmero: {num}")
            print("Divisores:", divisores)
            print("Quantidade de divisores:", len(divisores))
            print(primo)
            print(perfeito)

            pausa += 1

            if pausa == 10:
                continuar = input("\nContinuar? (sim/nao): ")
                if continuar.lower() != "sim":
                    break
                pausa = 0

            contador -= 1

    # ===============================
    # 2 – CALCULADORA SIMPLES
    # ===============================
    elif opcao == 2:
        print("\n=== CALCULADORA ===")
        print("Operações disponíveis: +  -  *  /")

        n1 = int(input("Introduza o primeiro número: "))
        n2 = int(input("Introduza o segundo número: "))
        oper = input("Operador (+,-,*,/): ")

        if oper == "+":
            print("Resultado =", n1 + n2)
        elif oper == "-":
            print("Resultado =", n1 - n2)
        elif oper == "*":
            print("Resultado =", n1 * n2)
        elif oper == "/":
            if n2 == 0:
                print("Erro: divisão por zero!")
            else:
                print("Resultado =", n1 / n2)
        else:
            print("Operador inválido!")

# ===================================================================================

    elif opcao == 3:
        limite = int(input("Introd um num inteiro entre 1 e 1000: "))

        while limite < 1 or limite > 1000:
            limite = int(input("Valor inválido! Introduza entre 1 e 1000: "))

        pausa = 0

        for i in range(1, limite + 1):
            print("\nTABUADA DO", i)
            for m in range(1, 11):
                print(i, "x", m, "=", i * m)

            pausa += 1

            if pausa == 20:
                continuar = input("\nParar? (s/n): ")
                if continuar.lower() == "s":
                    break
                pausa = 0

    elif opcao == 4:
        print("sair")

    else:
        print("Opção inválida!")
