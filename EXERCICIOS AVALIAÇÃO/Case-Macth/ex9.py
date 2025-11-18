req = {"metodo": "POST", "conteudo": ""}

if req["metodo"] == "GET":
    print("Requisição GET recebida")
elif req["metodo"] == "POST" and req["conteudo"]:
    print("Requisição POST com dados válidos")
elif req["metodo"] == "POST":
    print("Requisição POST sem dados")
else:
    print("Método não suportado")
