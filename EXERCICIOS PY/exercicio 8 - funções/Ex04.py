#4. Desenvolver uma função que receba a sigla do estado (Unidade Federativa) e retorne o nome do estado por extenso.

def nome_estado(sigla):
    sigla = sigla.upper()
    
    if sigla == "RS":
        return "Rio Grande do Sul"
    elif sigla == "SP":
        return "São Paulo"
    elif sigla == "GO":
        return "Goiás"
    elif sigla == "PR":
        return "Paraná"
    else:
        return "Sigla inválida!"
        
estado = input("Digite a sigla do estado: ")
nome = nome_estado(estado)
print(nome)