# Leitura dos dados
pontualidade = float(input("Digite o percentual de pontualidade (0 a 100): "))
produtividade = float(input("Digite nota de produtividade (0 a 10): "))

if pontualidade >= 90:
    if produtividade >= 8:
        desempenho = "Excelente"
    else:
        desempenho = "Bom"
elif pontualidade >= 70 and pontualidade <= 89 :
    if produtividade >= 6:
        desempenho = "Regular"
    else:
        desempenho = "Ruim"
else:  # pontualidade < 70
    desempenho = "Insatisfatório"

# Exibição do resultado
print(f"Classificação de desempenho: {desempenho}")

