#Desenvolva um algoritmo que lê 5 números e ao final, exibe a soma destes números.
soma = 0

for num1 in range (5): #O laço for vai rodar 5 vezes
    soma += float(input("Digite um numero: "))
print(f"A soma dos 5 numeros é {soma}")

