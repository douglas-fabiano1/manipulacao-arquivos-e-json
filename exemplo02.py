from encodings import utf_8
with open("dados.txt", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:
        lista = linha.split(",")
        print(f"Nome: {lista[0]}")
        print(f"Idade: {lista[1]}")
        print(f"Profissão: {lista[2]}")
        print(f"Salário: {lista[3]}")

print("\nArquivo fechado!")