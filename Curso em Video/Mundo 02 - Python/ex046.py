#Faça um programa que mostre na tela uma contagem regressiva de 10 à 0 com pausa de 1 segundo

from time import sleep

for cont in range(10, -1, -1):
    sleep(1)
    print(cont)
print('\033[32mFELIZ ANO NOVO!!!!!\33[m')