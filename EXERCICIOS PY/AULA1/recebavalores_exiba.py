#Receba dois valores, calcule e exiba os resultados das operações de soma, 
#subtração, divisão e multiplicação entre estes dois números.


num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

soma = num1 + num2 
print(f"Resultado da soma é: {soma:.0f}")

subtracao = num1 - num2
print(f"Resultado da subtração é: {subtracao:.0f}")

divisao = num1 / num2
print(f"Resultado da divisão é: {divisao:.0f}") #.0f tira virgula

multiplica = num1 * num2
print(f"Resultado da multiplicação é: {multiplica:.0f}")


