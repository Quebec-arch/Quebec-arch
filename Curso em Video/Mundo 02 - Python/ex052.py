#Faça um programa que leia um numero inteiro e diga ou não se ele é primo

'''num = int(input('Verifique se o numero escolhido é primo: '))
isPrime = True
current = (num // 2)
for i in range(current, 0, -1):
    if num % i == 0 and i != 1:
        isPrime = False
if isPrime:
    print('O numero é {} primo'.format(num))
else:
    print('O numero {} não é primo'.format(num))'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end= ' ')
        tot = tot + 1
    else:
        print('\033[31m', end= ' ')
    print(f'{c}', end= ' ')
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print(f'O número {num} é PRIMO')
else:
    print(f'O número {num} não é PRIMO')
