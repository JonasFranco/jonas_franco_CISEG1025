historico = []

def criptografar(mensagem, chave):
    soma_chave = 0
    for i in range(len(chave)):
        soma_chave = soma_chave + ord(chave[i])
        
    codigos = []
    for i in range(len(mensagem)):
        valor_letra = ord(mensagem[i])
        
        if valor_letra >= 32 and valor_letra <= 126:
            novo_valor = valor_letra + soma_chave
            while novo_valor > 126:
                novo_valor = novo_valor - 95
            codigos.append(novo_valor)
        else:
            codigos.append(valor_letra + soma_chave)
            
    return codigos

def descriptografar(codigos, chave):
    soma_chave = 0
    for i in range(len(chave)):
        soma_chave = soma_chave + ord(chave[i])
        
    texto = ""
    for i in range(len(codigos)):
        valor_codigo = codigos[i]
        
        if valor_codigo >= 32 and valor_codigo <= 126:
            valor_original = valor_codigo - soma_chave
            while valor_original < 32:
                valor_original = valor_original + 95
            texto = texto + chr(valor_original)
        else:
            texto = texto + chr(valor_codigo - soma_chave)
            
    return texto

def listar():
    if len(historico) == 0:
        print("Ainda nao existem registos.")
    else:
        for i in range(len(historico)):
            print(historico[i])

while True:
    print("    MENU")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("3 - Listar")
    print("4 - Sair")
    
    opcao = input("Opcao: ")
    
    if opcao == "1":
        msg = input("Mensagem: ")
        
        chv = ""
        while len(chv) == 0:
            chv = input("Chave: ")
            
        resultado = criptografar(msg, chv)
        print("Codigos: ", resultado)
        
        dicionario = {"mensagem": msg, "chave": chv, "codigos": resultado}
        historico.append(dicionario)
        
    elif opcao == "2":
        numeros_str = input("Codigos separados: ")
        
        chv = ""
        while len(chv) == 0:
            chv = input("Chave: ")
            
        partes = numeros_str.split()
        lista_numeros = []
        for i in range(len(partes)):
            lista_numeros.append(int(partes[i]))
            
        texto_final = descriptografar(lista_numeros, chv)
        print("Mensagem: ", texto_final)
        
    elif opcao == "3":
        listar()
        
    elif opcao == "4":
        break
    else:
        print("Opcao invalida")