#4.Leia 3 valores inteiros e diferentes e a seguir, encontre e exiba o maior, o menor e o intermediário.

num1 = int(input("Informe um número: "))
num2 = int(input("Informe um número: "))
num3 = int(input("Informe um número: "))

# Verifica se os números são diferentes
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Os números devem ser diferentes.")
else:
    # Encontra o maior
    if num1 > num2 and num1 > num3:
        maior = num1
    elif num2 > num1 and num2 > num3:
        maior = num2
    else:
        maior = num3

    # Encontra o menor
    if num1 < num2 and num1 < num3:
        menor = num1
    elif num2 < num1 and num2 < num3:
        menor = num2
    else:
        menor = num3

    # O intermediário é o que não é nem maior nem menor
    if (num1 != maior and num1 != menor):
        medio = num1
    elif (num2 != maior and num2 != menor):
        medio = num2
    else:
        medio = num3

    print(f"Menor: {menor}")
    print(f"Médio: {medio}")
    print(f"Maior: {maior}")
