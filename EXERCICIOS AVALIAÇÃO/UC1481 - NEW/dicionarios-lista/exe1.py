alunos = []

def inserir_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    curso = input("Digite o curso do aluno: ")

    if nome == "" or idade == "" or curso == "":
        print("Erro: Nenhum campo pode estar vazio.")
        return

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)
    print("Aluno inserido com sucesso!")

def listar_alunos():
    if len(alunos) == 0:
        print("Lista vazia.")
        return

    for aluno in alunos:
        print("\nnome:", aluno["nome"])
        print("idade:", aluno["idade"])
        print("curso:", aluno["curso"])

def menu():
    while True:
        print("\n1 - Inserir")
        print("2 - Listar")
        print("3 - Sair")

        opcao = input("Escolha: ")

        match opcao:
            case '1':
                inserir_aluno()
            case '2':
                listar_alunos()
            case '3':
                print("A sair...")
                break
            case _:
                print("Opção inválida.")

menu()