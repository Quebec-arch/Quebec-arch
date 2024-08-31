#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'São'

cidade = str(input('Digite o nome da cidade: ')).strip()
cidade = cidade.capitalize()
print('O nome da ciade é {}, ela começa com Santo? \n{} '.format(cidade, cidade.startswith('Santo')))