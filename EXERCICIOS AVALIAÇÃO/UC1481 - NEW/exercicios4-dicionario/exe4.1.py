lista_alunos = []

while True:
    print("1-Inserir 2-Listar 3-Sair")
    opcao = input("Opcao: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")
        
        aluno = {"nome": nome, "idade": idade, "curso": curso}
        lista_alunos.append(aluno)
        
    elif opcao == "2":
        it = 0
        while it < len(lista_alunos):
            print("nome:", lista_alunos[it]["nome"])
            print("idade:", lista_alunos[it]["idade"])
            print("curso:", lista_alunos[it]["curso"])
            print("-" * 10)
            it += 1
    elif opcao == "3":
        break