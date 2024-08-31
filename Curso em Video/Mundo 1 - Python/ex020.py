#O mesmo professor do desafio anterior que sortear a ordem de apresentação do trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
'''alunos = ['Andreza', 'Gabriel', 'Pedro', 'Flavia']
random.shuffle(alunos)
print('A ordem de apresentação será: {}'.format(alunos))'''

n1 = input('Primeiro aluno ')
n2 = input('Segunda aluno ')
n3 = input('Terceira aluno ')
n4 = input('Quarta aluno ')
lista = [n1, n2, n3, n4]
ordem = random.shuffle(lista)
print('A ordem de apresentação será \n {}'.format(lista))