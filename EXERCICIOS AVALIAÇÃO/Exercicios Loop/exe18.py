limite = int(input("Digite um número: "))

contador_perfeitos = 0

print("Números perfeitos encontrados:")

for n in range(1, limite + 1): 
    soma = 0

    for d in range(1, n):
        if n % d == 0:
            soma += d

    if soma == n:
        print(n)
        contador_perfeitos += 1

print(f"\nTotal de números perfeitos até {limite}: {contador_perfeitos}")
