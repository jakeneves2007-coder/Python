#lê o arquivo linha e armazena em uma lista

arquivo = open("Apresentacao.py")
linhas = arquivo.readlines()
for linha in linhas:
 print(linha)
    
#lê o texto completo do arquivo

arquivo = open("Apresentacao.py")
texto_completo = arquivo.read()
print(texto_completo)

<<<<<<< HEAD
#lê o arquivo linha por linha
=======
#lê o arquivo linha po linha
>>>>>>> d9bb805b2a3bf47831045b94994c84ce3eaddebd

arquivo = open("Apresentacao.py")
linha = arquivo.readline()
print(linha)
