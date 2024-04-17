
def votacao():
    candidatos = ["Débora", "Gabrielle", "Emanuel"]
    votos = [0, 0, 0]

    eleitores = int(input("Digite o número de eleitores: "))
    i = 0
    while i < eleitores:
        print("\n6 - Débora")
        print("12 - Gabrielle")
        print("13 - Emanuel")
        voto = int(input("Digite o número do candidato desejado: "))

        match voto:
            case 6:
                voto=1
            case 12:
                voto=2
            case 13:
                voto=3

        print(voto)
        if ((voto < 4) and (voto > 0)):
            indice = int(voto) - 1
            votos[indice] += 1
            print("\nVoto registrado para", candidatos[indice])
            i += 1
        else:
            print("Opção inválida!")

    print("\nResultado da votação:")
    for i in range(len(candidatos)):
        print(f"{candidatos[i]}: {votos[i]} votos")
    if (votos[0]==votos[1] and votos[0]>votos[2]) or (votos[0]==votos[2] and votos[0]>votos[1]) or (votos[1]==votos[2] and votos[1]>votos[0]) :
        print("\nEmpate!! Não houve candidato eleito")
    else:
        eleito = candidatos[votos.index(max(votos))]
    print("\nO candidato eleito é: ", eleito)

votacao()


