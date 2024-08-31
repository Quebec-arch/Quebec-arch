#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas. E com todas as letras minusculas.
#Quantas letras tem o nome (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
nome = nome.split()
print(nome[0], len(nome[0]))
