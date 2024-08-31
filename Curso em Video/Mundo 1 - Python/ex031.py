#Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem.
#Cobrando R$0,50 por Km para viagens ate 200Km e R$0,45 para viagens mais longas

viagem = float(input('Digite a distancia da viagem em kilometros: '))
if viagem <= int(200):
    print('O valor da viagem de {}km, será de R${}'.format(viagem, viagem * 0.50))
else:
    print('O Valor da viagem de {}km, será de R${}'.format(viagem, viagem * 0.45))
