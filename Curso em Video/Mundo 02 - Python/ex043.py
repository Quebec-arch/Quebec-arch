#Desenvolva uma logica que leia o peso e altura de uma >
#Abaixo 18.5 - Abaixo do peso:
#entre 18.5 e 25 - Peso ideal
#25 até 30 - sobrepeso:
#30 ate 40 - obesidade:
#acima de 40 - obesidade morbida

peso = float(input('Digite seu peso ' ))
altu = float(input('Digite sua altura '))
imc = peso / (altu * altu)
print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
  print('Abaixo do peso')
elif imc == 18.5 and imc <25:
  print('Peso Ideal')
elif imc >= 25 and imc <= 30:
  print('Sobrepeso')
elif imc >= 30 and imc < 40:
  print('Obesidade')
else:
  print('Obesidade Morbida')