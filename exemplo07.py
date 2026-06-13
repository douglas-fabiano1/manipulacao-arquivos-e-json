# Cadastrar os dados de alunos: matrícula, nome, três notas
# Calcular a média das notas
# Salvar as informações em arquivo json

# vou precisar importar do módulo json para criar o meu arquivo
import json

lista = []
print("### Cálculo de notas ###")
print("Para sair do programa digite 0 no campo matrícula")

# Preenchimento dos dados
while True:
    matricula = input("Digite a matricula: ")
    if matricula == "0":
        break  # finaliza o loop!
    nome = input("Informe o nome do aluno: ")
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    lista_notas = [nota1, nota2, nota3]
    media = round(sum(lista_notas) / len(lista_notas), 2)
    dicionario = {
        "Matricula": matricula,
        "Nome": nome,
        "Media": media,
        "Notas": lista_notas
    }

    # Insere o dicionario na lista
    lista.append(dicionario)
# Mostra a lista de dicionários
print(lista)

# Criação do arquivo json e armazenamento da lista de dicts nele
with open("cadastro_alunos.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista, arquivo, indent=4,
              ensure_ascii=False)  # o .dump pega a estrutura e converte para a equivalente ao json

# Leitura do json e transformação para o formato dict do Python
with open("cadastro_alunos.json", "r", encoding="utf-8") as arquivo2:
    lista = json.load(arquivo2)

    for dicionario in lista:
        print(f"Matricula: {dicionario["Matricula"]}")
        print(f"Nome: {dicionario["Nome"]}")
        print(f"Media: {dicionario["Media"]}")
        print(f"Notas: {dicionario["Notas"][0]}, {dicionario["Notas"][1]}, {dicionario["Notas"][2]}")
        print("---------------------------------------------")

# Mostra as informações do aluno
# print(f"\nMatricula: {dicionario["Matricula"]}\nNome do aluno: {dicionario['Nome']}")
# print(f"Notas do aluno: {dicionario["Notas"][0]}, {dicionario["Notas"][1]}, {dicionario["Notas"][2]}")
# print(f"Média do aluno: {dicionario["Media"]:.2f}\n\n")
