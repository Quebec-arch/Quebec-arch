#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = int(input('Digite o ano: '))
if ano % 4 == 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))