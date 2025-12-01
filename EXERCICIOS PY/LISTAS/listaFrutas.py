frutas = ["banana", "laranja", "pera"]

print(frutas[0]) # mostra a primeira fruta

print(frutas[-1]) # mostra a ultma fruta
print(frutas[2]) # mostra a ultima fruta
print(frutas[len(frutas)-1]) # mostra a ultima fruta

# mostra todas as frutas
for i in range(len(frutas)):
    print(frutas[i])



# forma facilitada a percorrer uma linha
for f in frutas:
    print(f)

print("Antes de modificar: ", frutas)
frutas[0] = "abacaxi"
print("Após modificar ", frutas)