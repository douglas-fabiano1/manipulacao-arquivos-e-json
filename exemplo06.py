# Criando um arquivo json

# Importo a lib json
import json
from textwrap import indent

lista = [10, 50, 449, 8, 2300, None, 5, 'Douglas', "Fabiano"]

dicionario = {
    "nome": "Paulo",
    "idade": 35,
    "altura": 1.80,
    "peso": 84.0,
    "profissao": "Estudante",
    "notas": [9, 10.0, 7.50]
}

with open("exemplo.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista, arquivo)

with open("exemplo-dict.json", "w", encoding="utf-8") as arquivo2:
    json.dump(dicionario, arquivo2)
