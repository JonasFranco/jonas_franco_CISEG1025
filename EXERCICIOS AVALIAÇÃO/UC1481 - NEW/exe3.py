nomes = ["Pedro Pereira","Ana Beatriz","Ana Clara","Carlos Silva","Beatriz Souza","Ana Paula","Pedro Andrade"]

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        if nomes[i] > nomes[j]:
            auxiliar = nomes[j]
            nomes.pop(j)
            nomes.insert(i, auxiliar)

print("Lista Ordenada:")
for i in range(len(nomes)):
    print(nomes[i])