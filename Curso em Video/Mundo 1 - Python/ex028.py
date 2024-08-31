#Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 a 5 e peça para o usuário
#tentar descobrir qual foi o numero escolhido pelo computador. O programa devera escrever
#na tela se o usuário venceu ou perdeu

import random
import time
escolha = input('Escolha um número entre 0 e 5: ').strip()
num = ['0', '1', '2', '3', '4', '5']
time.sleep(2)
num = random.choice(num)
print(num)
if escolha == num:
    print('Você esta certo!')
else:
    print('Você está errado!')

