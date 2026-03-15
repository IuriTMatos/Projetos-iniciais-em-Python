import random

opcoes = ["pedra", "papel", "tesoura"]

usuario = input("escolha pedra, papel ou tesoura: ").lower()

computador = random.choice(opcoes)

print("computador escolheu:", computador)

if usuario == computador:
        print("empate!")

elif (usuario == "pedra" and computador == "tesoura") or \
    (usuario == "tesoura" and computador == "papel") or \
    (usuario == "papel" and computador == "pedra"):
        print("você venceu")

elif usuario in opcoes:
        print("computador venceu")

else:
        print("opção invalida")
