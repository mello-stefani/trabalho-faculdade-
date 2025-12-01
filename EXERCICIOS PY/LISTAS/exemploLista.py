lista = [] #declara uma variavel lista vazia

while True:
    leitura = input("Informe um valor: ")
    if leitura == "":
        break
    lista.append(leitura)
print(lista)
