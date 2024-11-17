#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
menu = ('''Por gentileza selecione uma opção:
[ 1 ] Somar os números:
[ 2 ] Multiplicar os numero:
[ 3 ] Qual o numero Maior:
[ 4 ] Digite novos números:
[ 5 ] Fechar:''')
print(f'O numeros foram {num1} e {num2}')
print(menu)
user = int(input('Digite uma opção entre 1 e 5: '))

while user != 5:
    if user == 1:
        soma = num1 + num2
        print(f'A soma de ambos os números escolhidos é {soma}')
        user = int(input('Digite uma opção entre 1 e 5: '))
    if user == 2:
        mult = num1 * num2
        print(f'A multiplicação dos numeros escolhidos é {mult}')
        user = int(input('Digite uma opção entre 1 e 5: '))
    if user == 3:
        if num1 > num2:
            print('O primeiro valor é maior')
        elif num1 < num2:
            print('O segundo valor é maior')
        else:
            print('Ambos os valores são identicos')
        user = int(input('Digite uma opção entre 1 e 5: '))
    if user == 4:
        print('Digite os novos números: ')
        new_num1 = int(input('Digite o primeiro número: '))
        new_num2 = int(input('Digite o segundo número: '))
        num1 = new_num1
        num2 = new_num2
        print(f'Os novos números escolhidos foram {new_num1} e {new_num2}')
        user = int(input('Digite uma opção entre 1 e 5: '))
print('\033[31mOpção 5 selecionada. Programa encerrado\033[m')
