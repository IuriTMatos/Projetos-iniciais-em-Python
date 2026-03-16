import random

numero_secreto = random.randint(1, 100)


while True:
    try:
        palpite = int(input("Digite um número entre 1 e 100: "))

        if palpite < 1 or palpite > 100:
            raise ValueError("Número fora do intervalo")
        
        if palpite < numero_secreto:
            print("Número é maior")
        
        elif palpite > numero_secreto:
            print("Número é menor")
        
        else:

            print("Você Acertou")

            break
    except ValueError as erro:
        print("Entrada errada", erro)
