from encodings import utf_8
# abre o arquivo de texto
arquivo = open("dados.txt", "r", encoding="utf-8")

# lê o arquivo de texto e retorna em uma string
texto = arquivo.read()
print(texto)

# fecha o arquivo de texto
arquivo.close()
