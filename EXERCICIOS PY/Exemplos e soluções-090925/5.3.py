'''
Escreva um algoritmo que lê dois números e
em seguida exibe os números pares e os números
ímpares existentes entre estes dois números.
'''
a = int(input("Informe valor inicial do intervalo: "))
b = int(input("Informe valor final do intervalo: "))

pares = "Numeros pares: "
impares = "Numeros impares: "
for x in range(a, b) :
    if (x % 2 == 0) :
        pares +=  str(x) + " "
    else :
        impares +=  str(x) + " "
print(pares)
print(impares)





