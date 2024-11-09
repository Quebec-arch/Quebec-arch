#Desenvolva um programa que leia seis numeros inteiros e mostre apenas a soma daqueles que forem pares
#se o valor for impar desconsidere-o


s = 0
for i in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s += num
print('Soma dos valores é: {}'.format(s))