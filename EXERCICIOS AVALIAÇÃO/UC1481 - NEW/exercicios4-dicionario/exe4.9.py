notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

for aluno in notas.keys():
    lista_notas = notas[aluno]
    soma = 0
    it = 0

    while it < len(lista_notas):
        soma = soma + lista_notas[it]
        it += 1
    
    media = soma / len(lista_notas)
    print(aluno + ":", media)