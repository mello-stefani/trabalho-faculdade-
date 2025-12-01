# Solicita ao usuário um valor de pH entre 0 e 14
ph = int(input("Digite o valor do pH [entre 0-14]: "))



# Verifica se o valor está dentro do intervalo válido
if ph < 0 or ph > 14:
    print("Valor inválido! O pH deve estar entre 0 e 14.")
else:
    if ph > 7:
        print("Básico")
    elif ph < 7:
        print("Ácido")
    else:
        print("Neutro")
