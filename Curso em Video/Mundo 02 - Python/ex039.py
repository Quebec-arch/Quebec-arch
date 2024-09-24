#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#Se ele ainda vai se alistar // se é hora de se alistar // se já passou do tempo do alistamento
#Seu programa também deve mostrar o tempo que falta ou se já passou do prazo

from datetime import date
ano = date.today().year
nascimento = int(input('Digite seu ano de Nascimento: '))
idade = ano - nascimento
print('Sua idade é {}'.format(idade))
tempo = 18 - idade
prazo = idade - 18

if idade == 18:
    print('Esta na idade para alistamento militar')
elif idade < 18:
    print('Ainda não esta na hora do alistamento. Faltam {} ano (s) para seu alistamento'.format(tempo))
else:
    print('O prazo para se alistar foi há {} ano (s) atrás'.format(prazo))