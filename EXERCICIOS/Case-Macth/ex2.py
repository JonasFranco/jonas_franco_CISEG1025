nota = int(input("Digite sua nota de 0 a 100: "))

if nota < 0 or nota > 100:
    print("Nota inválida")
elif nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bom")
elif nota >= 50:
    print("Suficiente")
else:
    print("Insuficiente")
