# Cadastrar nome e a idade de várias pessoas
# Armazenar as informações

with open("cadastro.txt", "a", encoding="utf-8") as arquivo:
    print("Insira os nomes e idades das pessoas que deseja cadastrar!")
    print("Para sair, digite 'sair' no nome!\n")

    while True:
        nome = input("Digite o nome: ")
        if nome == "sair":
            break
        idade = int(input("Digite a idade: "))
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade}\n\n")

with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha)
