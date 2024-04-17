def contadorAbc():
    vogais = "a e i o u".split()
    consoantes = 0
    vogal = 0
    frase = input("Digite uma frase: ")
    for char in frase.lower():
        if char in vogais:
            vogal +=1
        elif not char.isspace():
            consoantes += 1

    print(f"A frase digitada foi '{frase}';")
    print(f"A Quantidade de vogais é de: {vogal}")
    print(f"A Quantidade de consoantes é de: {consoantes}")
contadorAbc()