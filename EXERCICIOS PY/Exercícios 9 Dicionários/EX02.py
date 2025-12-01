#Efetue a leitura de um texto a partir de um arquivo de entrada e apresenta a contagem da ocorrência de cada palavra do texto fazendo uso da estrutura de dados dicionário.

leitura_texto = {}

with open('leitura_texto.txt','r') as arquivo:
    texto = arquivo.read()

palavras = texto.lower().split()

for palavra in palavras:
    if palavra in leitura_texto:
        leitura_texto[palavra] += 1
    else:
        leitura_texto[palavra] = 1

for palavra, contagem in leitura_texto.items():
    print(f"{palavra}: {contagem}")



