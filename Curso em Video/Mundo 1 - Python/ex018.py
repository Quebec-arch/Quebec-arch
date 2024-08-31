#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians
angulo = float(input('Digite um anogulo de uma circunferencia '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo {} tem valor de seno igual à {:.2f}'.format(angulo, seno))
print('O angulo {} tem valor de cosseno igual à {:.2f}'.format(angulo, cosseno))
print('O angulo {} tem valor da tagente igual à {:.2f}'.format(angulo, tangente))