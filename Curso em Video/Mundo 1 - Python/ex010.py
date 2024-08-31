real = float(input('Quantos reais você possui? R$'))
print('Com R${} você pode comprar £{:.2f}'.format(real, real / 7.35))
print('Com R${} você pode comprar U${:.2f} '.format(real, real / 5.76))