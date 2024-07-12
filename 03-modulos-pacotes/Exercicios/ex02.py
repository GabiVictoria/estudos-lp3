from modulos import mod02

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = mod02.calc_imc(peso, altura)
classificacao = mod02.classe_imc(imc)
peso_ideal = mod02.calc_peso_ideal(altura)
diferenca_peso = peso - peso_ideal

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
if classificacao != "Peso normal":
    if diferenca_peso > 0:
        print(f"Você precisa perder {diferenca_peso:.2f} kg para atingir o peso normal.")
    else:
        print(f"Você precisa ganhar {-diferenca_peso:.2f} kg para atingir o peso normal.")
