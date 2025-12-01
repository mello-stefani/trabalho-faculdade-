qtdPassagens = int(input("Digite a quantidade de passagens que deseja comprar: "))
valorOriginal = float(input("Digite o valor da passagem: "))
valorPassagem = 0
 
if qtdPassagens > 50:
    valorDesconto = valorOriginal * 0.60
    valorPassagem = valorDesconto * 50
    qtdPassagens = qtdPassagens - 50
elif qtdPassagens < 50:
    valorDesconto = valorOriginal * 0.60
    valorPassagem = valorDesconto * qtdPassagens
    qtdPassagens = 0
 
if qtdPassagens != 0:
    valorPassagem = valorPassagem + (qtdPassagens * valorOriginal)
 
print(valorPassagem)