#Retornar se a String e composta unicamente de caracteres alfabéticos

texto = input("Informe um texto: ")

if texto.isalpha(): #Verifica se a string é composta apenas por letras
    print(f"O texto '{texto}' é composto apenas por caracteres alfabéticos.")
else:
    print("O texto informado não é composto por caracteres alfabéticos.")