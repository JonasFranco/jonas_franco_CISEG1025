notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

for aluno in notas:
    soma = 0
    lista_notas = notas[aluno]

    for nota in lista_notas:
        soma += nota

    media = soma / len(lista_notas)

    print(aluno + ":", media)