#6. Elaborar um função que receba um número inteiro com argumento e retorne se o mesmo é primo ou não.

def primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    
    if contador == 2:
        return True
    else:
        return False

numero = int(input("Digite um numero: "))

if primo(numero):
    print("É primo")
else:
    print("Não é primo")