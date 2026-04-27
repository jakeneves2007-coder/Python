#-----------------MENU DE OPÇÕES ---------------#

def mostrar_menu():
    print("\n=== DICIONÁRIO INTERATIVO ===")
    print("1 - Adicionar palavra")
    print("2 - Buscar significado")
    print("3 - Listar todas as palavras")
    print("4 - Remover palavra")
    print("5 - Sair")
#--------------ADICIONAR PALAVRAS-------------------------------#

def adicionar_palavra(dicionario):
    palavra = input("Digite a palavra: ").strip()
    if not palavra:
        print("Palavra inválida.")
        return
    
    if palavra in dicionario:
        print(f"'{palavra}' já existe no dicionário.")
        return
    
    significado = input("Digite o significado: ").strip()
    if not significado:
        print(" Significado inválido.")
        return
    
    dicionario[palavra] = significado
    print(f"'{palavra}' adicionada com sucesso!")
#--------------BUSCAR PALAVRAS-----------------------------------#
def buscar_palavra(dicionario):
    palavra = input("Digite a palavra para buscar: ").strip()
    significado = dicionario.get(palavra)
    if significado:
        print(f"{palavra}: {significado}")
    else:
        print(f"'{palavra}' não encontrada no dicionário.")
#-------------LISTA DE PALAVRAS--------------------------------#
def listar_palavras(dicionario):
    if not dicionario:
        print("O dicionário está vazio.")
        return
    print("\n=== LISTA DE PALAVRAS ===")
    for palavra, significado in sorted(dicionario.items()):
        print(f"- {palavra}: {significado}")
        
#-----------------------REMOVER---------------------------------#

def remover_palavra(dicionario):
    palavra = input("Digite o que quer remover: ").strip()
    if palavra in dicionario:
        del dicionario[palavra]
        print(f" '{palavra}' removida com sucesso.")
    else:
        print(f"'{palavra}' não encontrada.")
        
#---------------------------------------------------------------------------------

def main():
    dicionario = {}
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except:
            print(" Digite um número válido.")
            continue

        if opcao == 1:
            adicionar_palavra(dicionario)
        elif opcao == 2:
            buscar_palavra(dicionario)
        elif opcao == 3:
            listar_palavras(dicionario)
        elif opcao == 4:
            remover_palavra(dicionario)
        elif opcao == 5:
            print("TCHAUUUU...")
            break
        else:
            print("Opção inválida.")
#----------------------------------------#

main()
