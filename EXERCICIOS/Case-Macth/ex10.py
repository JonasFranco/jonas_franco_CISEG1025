print("Dentro da lista abaixo: \n Pedra \n Papel \n Tesoura \n Selecione a opção desejada:")

jog1 = input("Jogador 1: ")
jog2 = input("Jogador 2: ")

match (jog1,jog2):
    case ("Pedra","Tesoura") | ("Tesoura","Papel") | ("Papel","Pedra"):
        print("Jogador 1 venceu")
    case ("Tesoura","Pedra") | ("Papel","Tesoura") | ("Pedra","Papel"):
        print("Jogador 2 venceu")
    case _:
        print("Empate!")