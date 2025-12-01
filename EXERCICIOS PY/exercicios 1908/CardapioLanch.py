#Elabore um programa que lê o código do item pedido, a quantidade e calcula o valor a ser pago pelo lanche. Considera que, a cada execução, será solicitado apenas um item.

codigo = int(input("Digite o codigo do item que deseja: "))
quantidade = int(input("Digite a quantidade que deseja: "))
 
match codigo:
    case 10:
        totalPagar = 1.1  * quantidade
        print(f"Você escolheu ", quantidade , "itens do codigo ", codigo, "e devera pagar um total de ", totalPagar)
    case 11:
        totalPagar = 1.3 * quantidade
        print(f"Você escolheu ", quantidade , "itens do codigo ", codigo, "e devera pagar um total de ", totalPagar)
    case 12:
        totalPagar = 1.5 * quantidade
        print(f"Você escolheu ", quantidade , "itens do codigo ", codigo, "e devera pagar um total de ", totalPagar)
    case 13:
        totalPagar = 1.1 * quantidade
        print(f"Você escolheu ", quantidade , "itens do codigo ", codigo, "e devera pagar um total de ", totalPagar)
    case 14:
        totalPagar = 1.3 * quantidade
        print(f"Você escolheu ", quantidade , "itens do codigo ", codigo, "e devera pagar um total de ", totalPagar)
    case 15:
        totalPagar = 1.5 * quantidade
        print(f"Você escolheu ", quantidade , "itens do codigo ", codigo, "e devera pagar um total de ", totalPagar)
    case _:
        print("Selecione uma opção valida")