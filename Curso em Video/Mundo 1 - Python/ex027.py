#Faça um programa que leia o nome de uma pessoa, e mostrando em seguida o primeiro e ultimo nome

nome = str(input('Digite seu nome completo: ')).strip()
p = nome.split()
print('Prazer em te conhecer!')
print('Primeiro nome: {}'.format(p[0]))
print('Ultimo nome: {}'.format(p[len(p)-1]))
