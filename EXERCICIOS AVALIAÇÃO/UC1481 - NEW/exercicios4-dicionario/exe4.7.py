d = {'a': 1, 'b': 2, 'c': 3}
invertido = {}

for chave, valor in d.items():
    invertido[valor] = chave

print(invertido)