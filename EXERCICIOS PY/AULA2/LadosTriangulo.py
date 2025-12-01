#Ler 3 valores inteiros. Verificar se estes valores não formam um triângulo, neste caso, mostrar mensagem de erro. Caso contrário, apresentar mensagem identificando o tipo do triângulo formado (isósceles, equilátero ou escaleno)

a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    
    if a == b == c:
        print("Triângulo Equilátero (3 lados iguais).")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles (2 lados iguais).")
    else:
        print("Triângulo Escaleno (3 lados diferentes).")
        
else:
    print("Erro: Os valores informados não formam um triângulo.")