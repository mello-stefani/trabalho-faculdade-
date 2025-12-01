#1.Leia um texto interativamente através da linha de comando e retorna a contagem da ocorrência de cada letra do alfabeto no texto.

dicionario = {}


texto = input("Digite um texto qualquer: ")
for letra in texto:
    print(letra)

    if letra in dicionario:
        dicionario[letra] += 1 
    else: dicionario[letra] = 1

print(dicionario)
