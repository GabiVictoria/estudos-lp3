# importa tudo de matematica
import matematica

print(matematica.PI)
print(matematica.soma(10.0, 3.2))
print(matematica.subtrair(10.0, 3.2))

# importar apenas os elementos (constantes, funces, classes) necessarios 
# nesse caso nao precisa de "matematica."

#IMPORTANTE - vamos usar muito

from matematica import PI, subtrair  
# from matematica *

print(PI)
print(subtrair(10.0, 3.2))

# caso tenha conflito de nome
from matematica import PI as PI_MAT

PI = 999999

print(PI_MAT)
print(subtrair(10.0, 3.2))