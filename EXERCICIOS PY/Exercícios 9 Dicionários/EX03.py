#3 Desenvolva um tradutor simples de língua estrangeira

def exibir_menu():
    print("\n--- Tradutor---")
    print("1. Incluir nova palavra")
    print("2. Alterar tradução")
    print("3. Remover palavra")
    print("4. Traduzir palavra")
    print("5. Listar todas as palavras")
    print("6. Sair")

dicionario = {}

while True:
    exibir_menu()
    opcao = input("Escolha uma opção (1-6): ")

    if opcao == "1":
        palavra = input("Inclua uma nova palavra: ").strip().lower()
        if palavra in dicionario:
            print("Essa palavra já existe no dicionário.")
        else:
            traducao = input("Digite a tradução: ").strip().lower()
            dicionario[palavra] = traducao
            print("Palavra adicionada com sucesso.")

    elif opcao == "2":
        palavra = input("Digite a palavra que deseja alterar: ").strip().lower()
        if palavra in dicionario:
            nova_traducao = input("Digite a nova tradução: ").strip().lower()
            dicionario[palavra] = nova_traducao
            print("Tradução atualizada.")
        else:
            print("Palavra não encontrada no dicionário.")

    elif opcao == "3":
        palavra = input("Digite a palavra que deseja remover: ").strip().lower()
        if palavra in dicionario:
            del dicionario[palavra]
            print("Palavra removida.")
        else:
            print("Palavra não encontrada.")

    elif opcao == "4":
        palavra = input("Digite a palavra a ser traduzida: ").strip().lower()
        if palavra in dicionario:
            print(f"Tradução: {dicionario[palavra]}")
        else:
            print("Palavra não encontrada.")

    elif opcao == "5":
        if dicionario:
            print("\n--- Dicionário ---")
            for palavra, traducao in dicionario.items():
                print(f"{palavra} → {traducao}")
        else:
            print("O dicionário está vazio.")

    elif opcao == "6":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")


