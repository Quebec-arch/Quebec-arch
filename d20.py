#Criando um D20 basico // Creating a basic D20
from random import randint
from time import sleep

print('=.=' * 20)
dado = input('Press enter to roll the dice ')
nat = randint(1, 20)
print('Rolling')
sleep(2)
print(nat)
if nat == 1:
    print('\033[31mCritical Fail\033[m')
if nat == 20:
    print('\033[34mCritical Success\033[m')
