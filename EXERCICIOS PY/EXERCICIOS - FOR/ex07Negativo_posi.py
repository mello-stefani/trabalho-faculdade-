#Elaborar um algoritmo que leia 10 números diferentes de zero. Para cada número lido, o algoritmo deverá exibir uma mensagem informando se o número é positivo ou negativo. Caso o zero seja informado, este não deve ser contado como uma leitura válida e uma mensagem deve ser exibida ao usuário.

contador = 0  # conta números válidos
positivo = 0
negativo = 0

while contador < 10:
    numero = int(input("Digite um número diferente de zero: "))

    if numero == 0:
        print("Zero não é válido, tente novamente!")
    elif numero > 0:
        positivo += 1
        print("Esse número é POSITIVO.")
        contador += 1
    else:
        negativo += 1
        print("Esse número é NEGATIVO.")
        contador += 1
print("Total de positivos:", positivo)
print("Total de negativos:", negativo)





