vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}

total = 0

for mes in vendas:
    total += vendas[mes]

print("Total de vendas:", total)