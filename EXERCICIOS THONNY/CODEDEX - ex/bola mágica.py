#BOLA MÁGICA COM RANDOM

import random 

question = input("Perguntas: ")

random_number = random.randint(1,9)

if random_number == 1:
  resposta = "Yes - definitely."

elif random_number == 2:
  resposta = "It is decidedly so."

elif random_number ==3:
  resposta = "Without a doubt"

elif random_number ==4:
  resposta = "Reply hazy, try again."

elif random_number ==5:
  resposta = "Ask again later."

elif random_number ==6:
  resposta = "Better not tell you now."

elif random_number ==7:
  resposta = "My sources say no."

elif random_number ==8:
  resposta = "Outlook not so good"

elif random_number ==9:
  resposta = "Very doubtful."

else:
  resposta = "ERROR"

print("Magic 8 Ball: " + resposta)


