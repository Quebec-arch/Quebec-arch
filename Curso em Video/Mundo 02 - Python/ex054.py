#Crie um programa que leia o ano de nascimento de 7 pessoas, no final mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores
from datetime import date

atual = date.today().year
counter_jovem = 0
counter_adulto = 0

for i in range(1, 7 + 1):
    ano = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    if atual - ano >= 21:
        counter_adulto += 1
    elif atual - ano <= 21:
        counter_jovem += 1
print(f'Temos {counter_adulto} maiores e {counter_jovem} menores de idade')
