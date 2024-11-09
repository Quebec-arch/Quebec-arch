#Desenvolva um programa que leia o nome, idade e sexo de 4 pesoas e no final mostre:
#A media de idade do grupo // O nome do homem mais velho // Quantas mulheres tem menos que 20 anos
from six import print_

maioridadehomem = 0
nomevelho = ''
mediaidade = 0
somaidade = 0
totmulher = 0
for p in range(1, 5):
    print(f'-------- {p}º PESSOA --------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

mediaidade = somaidade / 4
print(f'A media de idade do grupo é {mediaidade} anos')
print(f'O homem mais velho é {nomevelho} com {maioridadehomem} anos')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos')