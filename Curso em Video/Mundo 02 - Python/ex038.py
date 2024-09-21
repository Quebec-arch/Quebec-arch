#Escreva um programa que leia dois numeros inteiros e compare os mostrando na tela uma mensagem
#O primeiro valor é maior // O segundo valor é menor // Não existe maior ou menor, os dois são iguais

from time import sleep
n1 = int(input('Primeiro '))
n2 = int(input('Segundo '))
print('Os números escolhidos são {} e {}'.format(n1, n2))
print('ANALISANDO')
sleep(1)

if n1 > n2:
    print('O primeiro valor é Maior')
elif n2 > n1:
    print('O segundo valor é Maior')
else:
    print('Não existe maior ou menor, ambos valores são iguais')
