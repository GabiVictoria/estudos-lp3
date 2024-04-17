import random
def dicionario():
    palavras = ["gato", "estante", "computador", "livro", "biblioteca", "pagina", "sala", "palindromo"]
    return random.choice(palavras)

def forca():
    palavra = dicionario()
    corretas = set(palavra)
    chances = 6
    descobertas = set()

    print("Forca!")
    while chances > 0:
        palavra_oculta = ''.join(letra if letra in descobertas else ' _' for letra in palavra)
        print(palavra_oculta)

        palpite = input("Digite uma letra ou a palavra completa: ").lower()

        if palpite == palavra:
            print("Parabéns! Você adivinhou a palavra.")
            print("A palavra correta era '{}'! ;)".format(palavra))
            break
        elif palpite in corretas:
            descobertas.add(palpite)
            if descobertas == corretas:
                print("Parabéns! Você adivinhou a palavra.")
                print("A palavra correta era '{}'! :)".format(palavra))
                break
        else:
            chances -= 1
            print("Essa letra não está na palavra. Você tem {} chances restantes.".format(chances))

    if chances == 0:
        print("Fim de jogo, quem sabe na próxima! A palavra correta era '{}'! :(".format(palavra))

forca()