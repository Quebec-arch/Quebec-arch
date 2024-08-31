#Escreva um programa que pergunte um salário de um funcionário e calcule o valor do seu aumento.
#Para salários maiores R$1.250,00 calcule um aumento de 10%. Para salários menores ou iguais o aumento é de 15%

sal = float(input('Digite o salário do colaborador R$'))
if sal > float(1250):
    aut = sal * 0.10 + sal
else: aut = sal * 0.15 + sal
print('O aumento será de R${}'.format(aut))

