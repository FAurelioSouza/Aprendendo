#16 Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcao inteira.

from math import trunc
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e a sua porcao inteira eh {}'.format (num, trunc(num)))

#17 Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do catedo adjacente: '))
hi = hypot(co ,ca)
print('A hipotunesa vai medir {:.2f}'.format(hi))

#18 faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))

#19 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2 ,n3, n4]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))

#20 Um Professor quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentacao sera ')
print(lista)
