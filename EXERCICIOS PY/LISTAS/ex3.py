# Leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas. Imprima-as.

lista = []
consoantes = []

for i in range(10):
    letra = input("Digite um caractere: ")
    lista.append(letra)
    
    # verifica se é letra e não é vogal
    if letra.isalpha() and letra not in "aeiou":
        consoantes.append(letra)

print("Foram lidas", len(consoantes), "consoantes.")
