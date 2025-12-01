#Verifique se a sequência de caracteres ___ encontra-se na String lida

frase = input("Digite uma frase: ")
caracter = "ao"

if caracter in frase:
    print(f"O caracter '{caracter}' foi encontrado na frase")
else:
    print(f"Caracter '{caracter}' não encontrada")