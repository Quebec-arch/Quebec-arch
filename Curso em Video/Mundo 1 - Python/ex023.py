#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

'''numero = int(input('Digite um numero de 0 a 9999: '))
print('Unidade {}'.format(numero[3]))
print('Dezena {}'.format(numero[2]))
print('Centena {}'.format(numero[1]))
print('Milhar {}'.format(numero[0]))'''

#Utilizar divisão inteira e resto para fatiar o numero de acordo

num = int(input("Digite um número a ser fatiado: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))