#5 Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um numero:'))
print('Analisando o valor {}, seu antecessor eh {} e o sucessor eh {}'.format (n, (n-1), (n+1)))

#6 Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um numero:'))
print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} eh igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))

#7 Desenvolva uum programa que leia as duas notas de um aluno, calcule e mostre a sua media.

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno:'))
media = (n1 + n2) / 2
print('a media entre {} e {} eh igual a {}'.format (n1, n2, media))

#8 Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

medida = float(input('Uma distancia em metros:'))
cm = medida * 100
mm = medida * 1000
print('Medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

#9 Faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um numero para ver sua tabuada: '))
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))

#10 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Quanto dinheiro voce tem na carteira? R$: '))
dolar = real / 5
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))

#11 Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m2

larg = float(input('Largura de uma parede: '))
alt = float(input('Altura de uma parede: '))
area = larg * alt
print('Sua parede tem a dimensao de {}x{} e a sua area eh de {}m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parade, voce precisara de {}l de tinta'.format(tinta))

#12 Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto

preco = float(input('Qual eh o preco do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}'.format(preco, novo))

#13 Faca um algoritmo que leia o salario deum funcionario e mostre seu novo salario, com 15% de aumento

salario = float(input('Qual o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)                     
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))

#14 Escreva ujm programa que converta uma temperatura digitada em C e converta para F

c = float(input('Informe a temperatura em C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {}C corresponde a {}F'.format(c, f))

#15 Escreva um programa que pergunte a quantidade de Km percorridos por um carrro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar eh de R${:.2f}'.format(pago))