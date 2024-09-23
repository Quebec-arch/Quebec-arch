#Elabore um programa que calcule o valor a ser pago
#por um produto considerando seu preço normal e
#forma de pagamento
#A vista - 10% de desconto
#A vista cartão - 5% de desconto
#Até 2x no cartão - preço normal
#3x ou mais - 20% de juros
from time import sleep
valor = float(input('Digite o valor do produto R$ '))
pag = str(input('Digite a forma de pagamento '))
print('O valor do produto é R${:.2f}'.format(valor))
print('e a forma de pagamento será via, {}'.format(pag))
sleep(1)

vista = (valor * 0.10) - valor
vcartao = valor * 0.5
cartax = valor
cartaoxx = (valor * 0.20) + valor

if 'vista' in  pag:
  print('O valor do produto será R${:.2f}'.format(vista))