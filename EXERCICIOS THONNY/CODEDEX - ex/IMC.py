#calculadora IMC


m = float(input("Informe seu peso: "))
a = float(input("Informe sua altura: "))

imc = m / (a ** 2)

print(f"Seu imc é: {imc:.2f}")