
# Lê 5 números e mostra na ordem inversa
num = []

for i in range(5):
    valor = int(input("Digite um número: "))
    num.append(valor)

print("Números na ordem inversa:")
print(num[::-1])   # jeito simples
