#Receber a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro...)

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

temperaturas = [] 

# Entrada das temperaturas
for i in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temp)  # adiciona na lista

# Cálculo da média anual
media_anual = sum(temperaturas) / len(temperaturas)
print(f"Média anual das temperaturas: {media_anual:.2f}°C")

# Mostrar meses acima da média
print("Meses com temperatura acima da média anual:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{i+1} – {meses[i]}: {temperaturas[i]:.2f}°C")

