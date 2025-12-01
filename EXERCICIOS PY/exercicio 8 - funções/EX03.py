#3. Elabore uma função que receba três valores representando os lados de um triângulo e retorne o tipo do triângulo.

def lado_triangulo(a,b,c):

    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
         return "Triângulo Equilátero: 3 lados iguais"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles: 2 lados iguais."
        else: 
            return "Triângulo Escaleno: lados diferentes. "
    else:
        return "ERRO! Os valores informados não formam um triângulo."

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

print(lado_triangulo(a,b,c))