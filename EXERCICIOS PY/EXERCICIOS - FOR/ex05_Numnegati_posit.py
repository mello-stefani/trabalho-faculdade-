#Desenvolva um algoritmo que leia 10 números e ao final da leitura, mostre quantos, dos números lidos são positivos e quantos são negativos.

positivo = 0
negativo = 0

for i in range(10): #repete 10 vezes
    numero = int(input(f"Informe o número: "))
    if numero >0:
        positivo += 1
    if numero <0:
        negativo += 1
# se for 0, não conta como positivo nem negativo

print(f"Quantidade de números positivos: {positivo}")
print(f"Quantidade de números negativos: {negativo}")
    

