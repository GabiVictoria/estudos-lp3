numero = float(input('digite o valor da compra '))

if numero >= 10 and numero< 100:
   desconto= numero*5/100
   valor=numero-desconto
elif numero >= 100 and numero< 500:
   desconto= numero*10/100
   valor=numero-desconto
elif numero >=500:
   desconto= numero*15/100
   valor=numero-desconto
else:
    desconto= 0.0
    valor=numero
   
print('o valor total com desconto é ', valor)
print('o desconto foi de ', desconto)
    

    