#Operadores Aritiméticos
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
