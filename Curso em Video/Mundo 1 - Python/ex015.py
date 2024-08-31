aluguel = int(input('Quantos dias o carro foi alugado? '))
kilometro = float(input('Quantos KMs o carro rodou? '))
dia = 60
Km = 0.15
total = (aluguel * dia) + (kilometro * Km)
print('O valor a pagar será de: R${:.2f}'.format(total))
