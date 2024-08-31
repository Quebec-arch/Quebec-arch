#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A' // Em que posição aparece pela primeira vez
#Em que posição aparece pela ultima vez

frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez em {}'.format(frase.lower().find('a')))
print('A letra A aparece na ultima posição em {}'.format(frase.lower().rfind('a')))