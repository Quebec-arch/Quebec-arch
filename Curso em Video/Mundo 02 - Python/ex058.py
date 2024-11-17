#Melhore o jogo do Desafio 28, onde o computador vai "pensar" em um numero entre 0 e 10, só que agora o jogador vai tentar advinhar
#até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint

computador = randint(0, 10)
print('Tente advinhar em qual número pensei entre 0 e 10')
tries = 0
acertou = False
while not acertou:
    jogador = int(input('Em qual número eu pensei? '))
    tries = tries + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
print(f'Parabens você acertou, o numero que pensei foi {computador}')
print(f'Foram necessários {tries} tantativas')
