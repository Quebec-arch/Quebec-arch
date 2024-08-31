#Faça um programa que leia o comprimento do cat op e do cat ad de um triangulo retangulo,
#e mostre o comprimento da hipotenusa.

from math import hypot

catetop = float(input('Digite o valor do cateto oposto '))
catetod = float(input('Digite o valor do cateto adjacente '))
print('A soma da Hipotenusa é de {:.2f}'.format(hypot(catetop, catetod)))

#segundo metodo

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hi))'''