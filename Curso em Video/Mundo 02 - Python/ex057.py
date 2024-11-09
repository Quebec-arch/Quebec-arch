#Faça um programa que leia o sexo de uma pessoa mas só aceite os valores M ou F, caso esteja errado peça
#a digitação novamente.

s = ' '
while s not in 'MmFf':
    s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
    if s != 'M' and s != 'F':
        print('Seleção invalida, por gentileza digite novamente')
    else:
        print('Obrigado, por gentileza aguarde!')


