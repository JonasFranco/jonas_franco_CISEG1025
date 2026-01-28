pala = input("Digite uma palavra: ")

if pala == "ola" or pala == "bom dia":
    print("saudação")
elif pala.endswith("?"):
    print("pergunta")
elif "adeus" in pala or "tchau" in pala:
    print("despedida")
else:
    print("mensagem genérica")
