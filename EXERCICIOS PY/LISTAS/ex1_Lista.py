#Leia números inteiros até que uma condição de parada seja atingida. Após, mostre-os.

numeros = []

while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:  # condição de parada
        break
    numeros.append(numero)

print("Números informados:", numeros)
