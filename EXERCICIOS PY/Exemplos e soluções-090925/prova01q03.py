premiototal = 2000000  # R$ 2.000.000,00

percentualsena = 0.62 # 62%
percentualquina = 0.22 # 22%
percentualquadra = 0.16 # 16%

# Solicita a quantidade de acertadores para cada faixa
acertadoressena = int(input("Digite a quantidade de acertadores da Sena (6 acertos): "))
acertadoresquina = int(input("Digite a quantidade de acertadores da Quina (5 acertos): "))
acertadoresquadra = int(input("Digite a quantidade de acertadores da Quadra (4 acertos): "))

# Calcula o valor destinado para cada faixa
premiosena = premiototal * percentualsena
premioquina = premiototal * percentualquina
premioquadra = premiototal * percentualquadra

# Exibe os resultados
print(f"\nValor para cada acertador:")
if acertadoressena > 0 :
    print(f"Sena (6 acertos): R$ {premiosena / acertadoressena}")
if acertadoresquina > 0 :
    print(f"Quina (5 acertos): R$ {premioquina / acertadoresquina}")
if acertadoresquadra > 0 :
    print(f"Quadra (4 acertos): R$ {premioquadra / acertadoresquadra}")
