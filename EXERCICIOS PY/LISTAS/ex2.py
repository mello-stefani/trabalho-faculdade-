#Leia uma lista de 10 números de ponto flutuante e mostre-os na ordem inversa.

lista = []

for f in range(10):
    numero = float(input("Informe um número: "))
    lista.append(numero)   # adiciona o número na lista

lista.reverse()  # inverte a ordem da lista

print("Números invertidos:")
for n in lista:
    print(n)
