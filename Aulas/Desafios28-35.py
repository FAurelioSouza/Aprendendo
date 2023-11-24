#28 Escreva um programa que faca o computador "pensar" em um numero inteira entre 0 e 5 e pca para o usuario tentar descobrir qual foi o numero escolhido pelo computador. Oprograma devera escrever na tela se o usuario venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente Advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens Voce me superou!')
else:
    print('Ganhei eu pensei no numero {} e nao no {}'.format(computador, jogador))

#29 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual eh a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! Voce excedeu o limite permitido que eh de 80km/h')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com cuidado')

#30 Crie um programa que leia um numero inteiro e mostre na tela se ele eh PAR ou IMPAR.

numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} eh PAR'.format(numero))
else:
    print('O numero {} eh IMPAR'.format(numero))

#31 Desenvolva um programa que pergunta a distancia de uma viagem em Km. Calcule o preco da passagem, cobrando R%0,50 por Km para viagens de ate 200Km e R%0,45 para viagens mais longas.

distancia = float(input('Qual eh a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {}Km.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia *0.45
print('Opreco da sua passagem sera de R${:.2f}'.format(preco))

#32 Faca um programa que leia um ano qualquer e mostre se ele eh BISSEXTO.

from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} eh BISSEXTO'.format(ano))
else:
    print('O ano {} nao eh BISSEXTO'.format(ano))

#33 Faca um programa que leia tres numeros e mostre qual eh o maior e qual eh o menor.

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero:'))
# Verificando o menor numero
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior numero
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digirado foi {}'.format(maior))

#34 Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R% 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento eh de 15%.

salario = float(input('Qual eh o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))

#35 Desenvolvam um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo.

print('-=' * 20)
print('Analisador de')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima nao podem formar um trianfulo')