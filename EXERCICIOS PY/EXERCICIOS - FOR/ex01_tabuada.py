#Desenvolva um algoritmo que exiba a tabuada de um número qualquer escolhido pelo usuário.

numero = int(input("Informe numero da tabuada: "))
print(f"Tabuada do {numero}")

for i in range (1,11): #serve para repetir um bloco de código para cada item de uma sequência
    print(f"{i} x {numero} = {i*numero}")


#------------

#OUTRO EXEMPLO 
#frutas = ["maçã", "banana", "laranja"]
#for fruta in frutas:
    #print(fruta)