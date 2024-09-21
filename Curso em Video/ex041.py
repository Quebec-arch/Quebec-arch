#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: 
#até 9 anos - MIRIM
#até 14 anos - INFANTIL 
#até 19 anos - JUNIOR 
#até 20 anos - SENIOR 
#acima - MASTER

from datetime import date
ano = date.today().year
nascimento = int(input('Digite seu ano de nascimento '))
idade = ano - nascimento
print('Idade {}'.format(idade))

if idade <= 9:
	print('Categoria Mirim')
elif idade <= 14:
	print('Categoria Infantil')
elif idade <= 19:
	print('Categoria Junior')
elif idade == 20:
	print('Categoria Senior')
else:
	print('Categoria Master')