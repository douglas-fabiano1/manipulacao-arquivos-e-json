# Criar um arquivo de texto
# função write cria o arquivo, se não existir, e só aceita string(str)
# caso já exista dados dentro do arquivo, ao ser executado, irá sobrescrever o conteúdo
# para que não sobrescrever, utilizo o "a" -> append
with open("exemplo_criado.txt", "w", encoding="utf-8") as arquivo:
    nome = input("Digite o seu nome: ")
    arquivo.write(f"Nome: {nome}\n")
    idade = input("Digite sua idade: ")
    arquivo.write(f"Idade: {idade}\n\n")  # ou arquivo.write(str(idade))
