d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

novo = {}

for chave in d1:
    novo[chave] = d1[chave]

for chave in d2:
    novo[chave] = d2[chave]

print(novo)