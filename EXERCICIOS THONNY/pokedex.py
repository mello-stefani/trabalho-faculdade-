pokedex = {
    "pikachu": {
        "tipo": "Elétrico",
        "número": 25,
        "descrição": "Um rato elétrico amarelo popular."
    },
    "charmander": {
        "tipo": "Fogo",
        "número": 4,
        "descrição": "Lagarto com fogo na cauda."
    },
    "bulbasaur": {
        "tipo": "Planta/Venenoso",
        "número": 1,
        "descrição": "Tem uma planta crescendo nas costas."
    },
    "gengar": {
        "tipo": "Fantasma/Venenoso",
        "número": 94,
        "descrição": "Sua forma é redonda e fantasmagórica, com braços curtos, pernas e uma expressão facial maligna."
    }

}

while True:
    nome = input("Escolha seu pokémon ou digite 'sair': ").lower()
    
    if nome == "sair":
        break
    elif nome in pokedex:
        pokemon = pokedex[nome]
        print(f"Número: {pokemon['número']}")
        print(f"Tipo: {pokemon['tipo']}")
        print(f"Descrição: {pokemon['descrição']}\n")
    else:
        print("Pokémon não encontrado. Tente novamente.\n")

# Usado .capitalize() para aceitar nomes como "pikachu", "charmander" etc. em minúsculo.
# ex: nome = input("Escolha seu pokémon ou digite 'sair': ").capitalize()


# == é uma comparação: verifica se o valor digitado é exatamente igual à string "sair".

#EXEMPLO do código: if nome.lower() == "sair":
# break