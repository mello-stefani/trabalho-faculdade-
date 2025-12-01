#Escreva um algoritmo que lê dois números e em seguida exibe os números pares e os números ímpares existentes entre estes dois números.

inicio = int(input("Informe inicio do intervalo: "))
fim = int(input("Informe fim do intervalo: "))


pares = f"Números pares entre {inicio} e {fim}: "
impares = f"Números impares entre {inicio} e {fim}: "

for i in range(inicio, fim + 1):
    if i % 2 ==0:
        pares += str(i) + " "


for i in range(inicio, fim + 1):
    if i % 2 !=0:
        impares += str(i) + " "

print(pares)
print(impares)