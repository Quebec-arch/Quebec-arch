#Escreve um programa para aprovar um emprestimo bancario para o comprador de uma casa. O programa vai perguntar
#O valor da casa, o salario do comprador e com quantos anos ele vai pagar: Calcule o valor mensal da prestação
#sabendo que ele não pode exceder mais de 30% do salario ou então o emprestimo será negado.

from time import sleep
print('Emprestimo para aprovação')
print('Se a prestação exceder 30% do seu salario, não poderemos aporvar o emprestimo')
valc = float(input('Digite o valor do imovél: R$'))
sal = float(input('Por favor insira seu salário: R$'))
temp = int(input('Em quantos anos pretende pagar: '))
print('--' * 20)

prestaçao = float(valc / (temp * 12))
exc = float(sal * 0.30)

print('O valor da prestação é de R${:.2f}'.format(prestaçao))
print('30% do seu salario equivale a R${:.2f}'.format(exc))
sleep(1)
if prestaçao >= exc:
    print('Sinto muito mas seu empretimo não foi aprovado')
else:
    print('Parabéns seu emprestimo foi aprovado')
