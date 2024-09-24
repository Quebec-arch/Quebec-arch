#Refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar qual triangulo será formado:
#Equilatero: todos os lados iguais
#Isosceles: dois lados iguais
#Escaleno: Todos os lados diferentes

a = int(input('Primeiro lado: '))
b = int(input('Segundo lado: '))
c = int(input('Terceiro lado: '))
if a + b > c and a + c > b and c + a > b:
    print('Esse triangulo existe!')
else:
    print('Esse triangulo não existe!')

print('Qual o tipo desse triangulo?')
if a == b and a == c and c == b:
    print('Equilatero')
elif (a == b) or (a == c) or (b == c):
    print('Isosceles')
else:
    print('Escaleno')