#Faça um programa que calcule a soma entre todos os numeros impares que se encontram no intervalo de 1 à 500

'''s = 0
for num in range(1, 501):
   if num % 2 != 0:
       if num % 3 == 1:
           s += num
print(f'Entre todos os {num} valores a soma deles é {s}')'''

soma = 0 #ACUMULADOR
cont = 0 #CONTADOR
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        cont += 1
print(f'A soma dos {cont} valores é de {soma}')
