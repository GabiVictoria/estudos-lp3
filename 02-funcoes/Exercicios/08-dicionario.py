def dicionario(conteudo):
    
    contagem = {}
    conteudo = conteudo.lower()
    palavras = conteudo.split()
    
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem

texto = input("Digite o seu texto: ")
resultado = dicionario(texto)
print(resultado)