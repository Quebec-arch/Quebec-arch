#Faça um programa que leia 3 números e mostre qual é o MAIOR e qual é o MENOR

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and a < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior))