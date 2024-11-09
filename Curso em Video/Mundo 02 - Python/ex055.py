#Faça um programa que leia o peso de 5 pessoas. No final mostre qual o maior e o menor peso lido

menor = 0
maior = 0

for i in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso é {maior}kgs')
print(f'O menor peso é {menor}kgs')