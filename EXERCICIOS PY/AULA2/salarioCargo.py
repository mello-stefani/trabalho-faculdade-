#Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. Leia o salário e o cargo de um funcionário e calcule o novo salário. Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 40% de aumento. Mostre o salário antigo, o novo salário e a diferença. 

#Código  Cargo Percentual 
#101	Gerente	10%
#102	Engenheiro	20%
#103	Técnico	30%

salario = float(input("Digite o salario: "))
cargo = float(input("Digite o cargo: "))

if cargo == 101:
    print("Gerente")
    percentual = 0.10
elif cargo == 102:
    print("Engennheiro")
    percentual = 0.20
elif cargo == 103:
    print("Técnico")
    percentual = 0.30
else:
    print("Outro cargo")
    percentual = 0.40

novoSal = salario * (1 + percentual)
diferenca = novoSal - salario

print(f"Salário antigo: R$ {salario:.2f}")
print(f"Novo salário: R$ {novoSal:.2f}")
print(f"Aumento: R$ {diferenca:.2f}")