#Crie um programa que leia o nome de uma pessoa e diga se tem 'Silva' nele

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome é {} e possui silva?'.format(nome))
if 'silva' in nome.lower():
    print('True')
else:
    print('False')


'''nome = str(input("Digite seu nome: \n"))
nome = nome.lower()
print("silva" in nome)'''