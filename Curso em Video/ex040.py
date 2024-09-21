#Crie um programa que leia duas notas de um aluno e calcule sua media. MOstrando uma mensagem no final de acordo com a Media atingida: 
#Abaixo de 5.0 alino REPROVADO 
#entre 5.0 e 6.9 aluno em RECUPERAÇAO 
#acima de 7.0 APROVADO

n1 = float(input('Primeira nota '))
n2 = float(input('Segunda nota '))
media = (n1 + n2) / 2
print('Sua nota é {}'.format(media))
if media < 5:
	print('Aluno REPROVADO')
elif media >= 5 and media <= 6.9:
	print('Aluno em RECUPERAÇÃO')
elif media >= 7:
	print('Aluno APROVADO')