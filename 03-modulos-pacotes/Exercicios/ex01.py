from modulos import mod01

comprimento = float(input("Digite o comprimento do aquário (cm): "))
altura = float(input("Digite a altura do aquário (cm): "))
largura = float(input("Digite a largura do aquário (cm): "))
temp_desejada = float(input("Digite a temperatura desejada (°C): "))
temp_ambiente = float(input("Digite a temperatura ambiente (°C): "))

volume = mod01.volume(comprimento, altura, largura)
potencia = mod01.potencia(volume, temp_desejada, temp_ambiente)
filtragem = mod01.filtragem(volume)

print(f"Volume do aquário: {volume:.2f} litros")
print(f"Potência do termostato: {potencia:.2f} watts")
print(f"Quantidade de filtragem por hora: {filtragem:.2f} litros")