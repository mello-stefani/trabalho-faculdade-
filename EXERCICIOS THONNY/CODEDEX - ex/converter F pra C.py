#CONVERTER F para celsius

temperatura = float(input("Informe a temperatura em Fahrenheit: "))

# Fórmula de conversão: (F - 32) / 1.8
celsius = (temperatura - 32) / 1.8

print(f"A temperatura convertida é: {celsius:.2f} °C")