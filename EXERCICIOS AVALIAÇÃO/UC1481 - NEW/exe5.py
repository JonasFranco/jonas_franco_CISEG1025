import os as operating
import json
import re as reg

filename = "dados.json"
file_saida_json = "validos.json"
file_saida_txt = "contactos.txt"

objecto = []
if operating.path.exists(filename):
    with open(filename, 'r', encoding='utf-8') as manipfile:
        objecto = json.load(manipfile)

print("Dados lidos do ficheiro:")
print(objecto)

registos_validos = []

it = 0
while it < len(objecto):
    item = objecto[it]
    
    email = item["email"]
    nif = item["nif"]
    telemovel = item["telemovel"]
    site = item["site"]
    
    padrao_email = r"^[\w\.]+@[\w]+\.\w+$"
    email_valido = reg.match(padrao_email, email)
    
    padrao_nif = r"^[123568][0-9]{8}$"
    nif_valido = reg.match(padrao_nif, nif)
    
    apenas_numeros = ""
    i_tel = 0
    while i_tel < len(telemovel):
        if telemovel[i_tel] >= "0" and telemovel[i_tel] <= "9":
            apenas_numeros = apenas_numeros + telemovel[i_tel]
        i_tel += 1
    
    tel_valido = False
    if len(apenas_numeros) == 9:
        tel_valido = True

    dominio = ""
    partes_site = site.split("//")
    if len(partes_site) > 1:
        dominio = partes_site[1]
    print("Dominio:", dominio)

    if email_valido and nif_valido and tel_valido:
        registos_validos.append(item)
    
    it += 1

with open(file_saida_json, 'w', encoding='utf-8') as manipfile:
    json.dump(registos_validos, manipfile, indent=4, ensure_ascii=False)

texto_acumulado = ""
it = 0
while it < len(objecto):
    linha = objecto[it]["nome"] + " - " + objecto[it]["email"] + "\n"
    texto_acumulado = texto_acumulado + linha
    it += 1

with open(file_saida_txt, 'w', encoding='utf-8') as manipfile:
    manipfile.write(texto_acumulado)

print("Feito")
