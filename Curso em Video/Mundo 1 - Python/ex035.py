a = int(input('Digite o valor do primeiro lado: '))
b = int(input('Digite o valor do segundo lado: '))
c = int(input('Digite o valor do terceiro lado: '))
if a + b > c and a + c > b and c + b > a:
		print ('O triangulo existe')
else:
		print('O triangulo não existe')
		