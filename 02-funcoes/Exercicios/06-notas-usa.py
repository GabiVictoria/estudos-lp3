
def notaUsa(nota_original):
    
    if nota_original >= 90:
        return "A"
    elif nota_original >= 80:
        return "B"
    elif nota_original >= 70:
        return "C"
    elif nota_original >= 60:
        return "D"
    else:
        return "F"
nota_conceito = float(input("Digite a sua nota na escala de 0 a 100: "))
nota = notaUsa(nota_conceito)
print(f"A nota no padrão por letras correspondente à nota informada é: {nota}")