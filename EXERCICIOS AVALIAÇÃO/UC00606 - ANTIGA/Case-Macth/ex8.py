print("Soma\nSubtracao\nMultiplicacao\nDivisao ")
opc = input("Escolha uma das opcoes: ")

num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))

if opc == "Soma":
    print(num1 + num2)
elif opc == "Subtracao":
    print(num1 - num2)   
elif opc == "Multiplicacao":
    print(num1 * num2)
elif opc == "Divisao":
    print(num1 // num2)