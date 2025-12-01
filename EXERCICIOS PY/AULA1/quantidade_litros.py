#Calcule a quantidade de cerveja, em litros, consumida por um bloco de carnaval.
#Para isso, considere que uma garrafa de cerveja possui 600ml e uma caixa possui 24 garrafas. 
#O algortimo deverá ler a quantidade de caixas consumidas e retornar a quantidade equivalente em litros.

garrafa = 600 
caixa = 24 

quantidade = int(input("Qual a quantidade de caixas consumidas: "))
multiplica = garrafa*caixa*quantidade

print("Quantidade de mililitros consumidas: ",multiplica)

retornaQuantidade = multiplica/1000
print(f"Quantidade retornada em litros é equivalente a: {retornaQuantidade}")










