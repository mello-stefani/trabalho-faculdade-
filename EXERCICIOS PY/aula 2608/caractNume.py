#Retornar se a String é composta unicamente de caracteres numéricos

texto = input("Informe um texto: ")

if texto.isnumeric(): #Verifica se a string é composta apenas por numeros
    print(f"O texto '{texto}' é composto apenas por caracteres numéricos.")
else:
    print("Esse texto não é composto por caracteres numéricos.")

