#1. Leia um valor inteiro e em seguida apresenta uma mensagem se o número é PAR ou IMPAR.

num1 = int(input("Digite um numero: "))

if num1 % 2 == 0:  #O símbolo % mostra quanto sobra depois de uma divisão.
    print("É par")
else:
    print("É ímpar")