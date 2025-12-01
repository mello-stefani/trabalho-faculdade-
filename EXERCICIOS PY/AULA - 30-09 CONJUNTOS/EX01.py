#1.Elabore uma aplicação para manter uma lista de compras utilizando a estrutura de conjuntos com as seguintes funcionalidades:


#a. adicionar item (se o item já estiver no conjunto, mostrar mensagem)
#b. remover item
#c. exibir todos os itens
#d. ordernar o conjunto alfabeticamente
#e. verificar se um item está contido em um conjunto

compras = set()

menu = """
1. Adicionar item
2. Remover item
3. Exibir itens
4. Ordenar
5. Verificar se item está no conjunto
6. Gravar 
7. Ler 
9. Finalizar

"""

while True:
    print(menu)
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        item = input("Adicione o item: ").strip().lower()
        if item in compras:
            print(f"{item} já está na lista.")
        else:
            compras.add(item)
            print(f"{item} adicionado.")

    elif opcao == "2":
        item = input("Remover item: ").strip().lower()
        if item in compras:
            compras.remove(item)
            print(f"{item} removido.")
        else:
            print(f"{item} NÃO está na lista.")

    elif opcao == "3":
        if compras:
            print("Itens na lista: ")
            for item in compras:
                print(item)
        else: 
            print("Lista vazia")

    elif opcao == "4":
        if compras:
            print("Itens na lista ordenadas:")
            for item in sorted(compras):
                print(f"- {item}")
        else:
            print("Lista vazia.")

    elif opcao == "5":
        item = input("Verificar item: ").strip().lower()
        if item in compras:
            print(f"{item} já está na lista de compras.")
        else:
            print(f"{item} NÃO está na lista")

    elif opcao == "6":
        arquivo = open ("C:\temp\lista.txt", "w")
        for i in compras:
            arquivo.write(i + "\n")
        arquivo.close()

    elif opcao == "7":
        arquivo = open ("C:\temp\lista.txt", "r")
        compras.clear()
        for i in arquivo.readlines():
            compras.add(i.replace( "\n", ""))

    elif opcao == "9":
        print("Finalizado!")
        break


            
            

        

    
    



    

    
    


