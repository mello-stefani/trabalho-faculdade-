#2. Leia dois valores inteiros e diferentes em seguida apresenta o MAIOR e o MENOR número.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if num1 == num2:
    print("Informe numeros diferentes")
else: 
    if num1 > num2: 
        print(f"{num1} é maior que {num2}")
    else:
        num1 < num2
        print(f"{num1} é menor que {num2}")


