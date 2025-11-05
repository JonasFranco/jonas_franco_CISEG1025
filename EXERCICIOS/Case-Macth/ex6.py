status = input("Enter status : ")
tempo = int(input("Enter tempo : "))

# if status == "ola" or status == "bom dia":
#     print("saudação")

if status == "ok" and tempo > 200:
    print("Servidor lento")
elif status == "ok":
    print("Servidor ativo")
elif status == "erro":
    print("Servidor indisponível")
else:
    print("Estado desconhecido")