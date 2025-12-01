#Exemplo de função

def minhafuncao():
    print("Exemplo de função")

def outrafuncao(nome):
    print("Argumento recebido:", nome)

def soma(num1,num2):
    return num1 + num2

def numeros(*num):
    for i in num:
        print(i)
#print(f"Recebi {(len(num))} argumentos")

minhafuncao()
outrafuncao("Stéfani")
print(soma(1,5))
numeros(1,2,3,4,5,6)