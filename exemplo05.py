# lib para manipular arquivos json
import json

# Leitura de um arquivo Json existente
with open("dados.json", "r", encoding="utf-8") as arquivo:
    # Lê os dados no arquivo e converte para o equivalente em Python
    # Ex: 'null' no json vira 'none' em Python
    lista = json.load(arquivo)

    # Imprimindo todos os elementos da lista de dicionários
    for dicionario in lista:
        print(f"Nome: {dicionario["Nome"]}")
        print(f"Idade: {dicionario["Idade"]}")
        print(f"Profissão: {dicionario["Profissao"]}")
        print(f"Salário: R$ {dicionario["Salario"]:.2f}")
        print("---------------------------------------------")

    # Imprimindo o item através da posição na lista
    print(f"\n{lista[0]}")