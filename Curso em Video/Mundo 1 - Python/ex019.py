#Um professor que sortear um de seus 4 aluno para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolido

import random

'''alunos = ('Andreza', 'Gabriel', 'Pedro', 'Flavia')
print(random.choice(alunos))
input('Confime a seleção, Y, N: ')'''

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
