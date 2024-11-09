#Refaça o desafio 9 mostrando a tabuada de um numero que o usuario escolher só que utilizando FOR

from time import sleep
num = int(input('Selecione a Tabuada a ser mostrada: '))
for t in range(0, 11):
    res = num * t
    sleep(0.5)
    print(f'{t} x {num} = {res}')
