
def volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def potencia(volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)

def filtragem(volume):
    return volume * 3 


