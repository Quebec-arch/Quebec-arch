#Escreve um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
#que ele foi multado, a multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Velocidade do veiculo: '))
limite = '80'
multa = 7 * (velocidade - 80)
if velocidade >= float('80'):
    print('Você está acima do limite permitido de {}Km/h.'.format(limite))
    print('Deverá pagar uma multa no valor de R${:.2f}'.format(multa))
else:
    print('Você esta dentro do limite permitido, tenha uma boa viagem!')