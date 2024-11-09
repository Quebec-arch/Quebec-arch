#Crie um programa que jogue Jokenpô com você

from random import choice
from time import sleep
jokenpo = ['Pedra', 'Papel', 'Tesoura']
joken = choice(jokenpo)
print('====' * 5, 'Jokenpo', '====' * 5)

print('''
Digite 1 para PAPEL
Digite 2 para PEDRA
Digite 3 para TESOURA ''')
jogador = int(input('Faça sua escolha: '))
if jogador == 1:
    print('Papel')
elif jogador == 2:
    print('Pedra')
elif jogador == 3:
    print('Tesoura')
print('Maquina:')
sleep(1)
print(joken)
print('Resultado')

if joken == 'Pedra' and jogador == 1:
    print('\033[34mParabéns, você Venceu!\033[m')
elif joken == 'Pedra' and jogador == 3:
    print('\033[31mInfelizmente você Perdeu!\033[m')
elif joken == 'Pedra' and jogador == 2:
    print('\033[\033[m')
elif joken == 'Papel' and jogador == 1:
    print('\033[32mEmpate\033[m')
elif joken == 'Papel' and jogador == 2:
    print('\033[34mParabéns, você Venceu!\033[m')
elif joken == 'Papel' and jogador == 3:
    print('\033[31mInfelizmente você Perdeu!\033[m')
elif joken == 'Tesoura' and jogador == 1:
    print('\033[31mInfelizmente você Perdeu!\033[m')
elif joken == 'Tesoura' and jogador == 2:
    print('\033[34mParabéns, você Venceu!\033[m')
elif joken == 'Tesoura' and jogador == 3:
    print('\033[32mEmpate\033[m')
