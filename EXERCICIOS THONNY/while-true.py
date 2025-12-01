#VALIDAÇÃO NOME

while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        print(f"{nome} é um nome válido.")
        break
    else:
        print("ERRO! Nome inválido. Deve ter mais de 3 letras.")

#VALIDAÇÃO IDADE

while True:

    idade = int(input("Digite sua idade: "))
    if 0<= idade <=150:
     print(f"{idade} Idade entre 0 a 150 anos")
     break

    else:
     print("ERRO! Iddade inválida")

#VALIDAÇÃO SALARIO

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        print(f"R${salario:.2f} salário válido")
        break

    else:
     print("ERRO! Salário não pode ser zero")


#VALIDAR ESTADO CIVIL - upper

while True:
    estado_civil = input("Seu estado civil (s/c/v/d): ").upper()
    if estado_civil in ['S', 'C', 'V', 'D']:
        print(f"{estado_civil} é um estado civil válido.")
        break
    else:
        print("Erro! Estado civil não encontrado. Use: S, C, V ou D.")

#VALIDAR ESTADO CIVIL - lower

while True:
    estado_civil = input("Seu estado civil (s/c/v/d): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        print(f"{estado_civil} é um estado civil válido.")
        break
    else:
        print("Erro! Estado civil não encontrado. Use: s, c, v ou d.")
