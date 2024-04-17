# Operadores aritméticos
# +, -, *. /, **

nota1 = 10.0
nota2 = 5.5
nota3 = 7.5
media = (nota1 + nota2 + nota3) / 3

# numero elevado a outro 
# e elevado a n
# 10 elevado a 2

numero = 10
numero_elevado_2 = numero * numero
numero_elevado_2 = numero ** 2

# Operadores Lógicos
# and, or, not

print(3 + 2) # 5
print(True and True)    #True
print(True and False)   #False
print(False and True)   #False
print(False and False)  #False

print(True or True)    #True
print(True or False)   #True
print(False or True)   #True
print(False or False)  #False

print(not True)     #False
print(not False)    #True

# é possível usar operadores boleanos em varáveis, mesmo que esteja fora de estruturas condicionais
# exemplo de código usado no mercado, inclusive em teste de correções

# 1º caso: permitir entrada se
# - o usuário for um funcionário E
# - o usuário não estiver bloqueado E
# - a hora atual estiver entre 8h e 18h

# 2º caso: permitir entrada se 
# - o usuario for um admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False

horario_comercial = hora_atual >= 8 and hora_atual <= 18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado

#if usuario_funcionario and not (usuario_bloqueado and hora atual >= 8 and hora_atual <= 18) or usuario_admin:

#if usuario_admin or (usuario_funcionario and not usuario_bloqueado and hora atual >= 8 and hora_atual <= 18):

#if usuario_admin or (usuario_funcionario and not usuario_bloqueado and horario_comercial):

if usuario_admin or (funcionario_ativo and horario_comercial):
    print('acesso permitido')

# pass

idade = 22
maior_idade = idade >= 18
if maior_idade: 
    pass

# Operadores de comparação
# ==, !=, >, <, >=, <=

# == compara valores -> se eles são iguais
# = atribuição

idade = 25
maior_idade = idade >= 18 #True

nota1 = 10.0
nota2 = 5.5
nota3 = 7.5
media = (nota1 + nota2 + nota3) /3

if media >= 6.0:
    print('aprovado')

# Operador de identidade
# is, is not
# comparar objetos que ocupam o mesmo espaço de memória

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) #True
print(a is b) #False

a == b
print(a is b) #True

# Operador in, not in
# verificar se um elemento existe ou não em uma sequência
# str, liste, tuple

opcoes = ('sim', 'não', 'talvez')
opcao = input('digite uma opcao')   # "     Sim     "
opcao = opcao.lower                 # "     sim     " 
opcao = opcao.strip                 # "sim"

# lower: deixa todos os caracteres em minúsculo
# strip: retira todos os espaços em branco

# o ideal é permitir que o usuário clique em opções ao invés de escrever, para evitar erros

if opcao in opcoes:
    print('ok')
else:
    print('nao tem essa opcao')

numeros = [1, 3, 5, 6]
for numero in numeros:
    print(numero)

# obs: o in, no for, cumpre a função do for each#Operadores Aritiméticos
nota1 = 10.0
nota2 = 5.5
nota3 = 7.5
media = (nota1 + nota2 + nota3)/3
numero = 10 
numereo_elevado_2 = numero*numero
numereo_elevado_2 = numero**2
#Operadores Lógicos

print(3+2)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or False)
print(False or True)

print(not True)
print(not False)

#permitir entrada

hora_comercial = hora_atual >=8 and hora_atual <=18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado
usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False

if usuario_admin or (funcionario_ativo and hora_comercial):
    print('acesso permitido')

    idade = 22
    maior_idade =idade >=18
    if maior_idade:
        pass 


    #Operadores de Comparação


# is, is not 
#operador de identidade que compara se os objetos ocupam os mesmo espaço de memória

a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
c=b 
print(b is c)

# operador in, not in
# verifica se olemento existe ou não em uma sequência
# str, list, tuple
opcoes = ('sim', 'nao', 'talvez')
opcao = input('Digite uma opcao')
opcao = opcao.lower()
opcao = opcao.strip()

if opcao in opcoes:
    print('ok')
else:
    print('nao tem essa opcao')
