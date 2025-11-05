print("eletronico\ncomun\nalimentar")
item = input("Insira uma das categorias validas, acima:")
valor = int(input("Insira o valor do produto:"))
                  

if item == "eletronico" and valor > 1000:
    print("Produto de luxo") 
elif item == "eletronico" and valor <= 1000:
    print("Produto comum")
elif item == "alimentar":
    print("Produto alimentar")
elif item == "_":
    print("Categoria invalida")
