import random

def advinhe():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
       
        if palpite < numero_secreto:
            print("Seu palpite está baixo. Por favor tente novamente.")
        elif palpite > numero_secreto:
            print("Seu palpite está alto. Por fravo tente novamente.")
        else:
            print(f"Parabéns!!! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
            break

        tentativas += 1
advinhe()
