def palindromo(texto):
    # Remove espaços e converte p/ minusculas
    texto = texto.replace(" ", "").lower()
    
    # Verifica com o inverso
    return texto == texto[::-1]

def main():
    entrada = input("Digite uma palavra ou frase: ")
    if palindromo(entrada):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
main()
