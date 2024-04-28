# APROVANDO IMPRESTIMO
#36 Escreva um programa para aprovar o emprestimo bancareio para a compra de uma casa. Pergune o valor da casa, o salario do comprador e em quantos anos ele vai pagar. A prestacao mensal, nao pode exceder 30% do salario ou entao o emprestimo sera negado.

def imprestimo():
    casa = float(input('Valor da casa: R$'))
    salario = float(input('Salario do comprador: R$'))
    anos = int(input('Quantos anos de financiamento? '))
    prestacao = casa / (anos * 12)
    minimo = salario * 30 / 100
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
    print(' a prestacao sera de R${:.2f}'.format(prestacao))
    if prestacao <= minimo:
        print('Emprestimo pode ser CONCEDIDO!')
    else:
        print('Emprestimo NEGADO!')
    
# CONVERSOR DE BASES NUMERICAS   
#37 Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao: 1 para binario, 2 para octal e 3 para hexadecimal.

def conversor():
    num = int(input('Digite um numero inteiro: '))
    print('''Escolha uma das bases para conversao:
    [ 1 ] converter para binario
    [ 2 ] converter para octal
    [ 3 ] converter para hexadecimal''')
    opcao = int(input('Sua opcao: '))
    if opcao == 1:
        print('{} convertido para BINARIO eh igual a {}'.format(num, bin(num)[2:]))
    elif opcao == 2:
        print('{} convertido para OCTAL eh igual a {}'.format(num, oct(num)[2:]))
    elif opcao == 3:
        print('{} convertido para HEXADECIMAL eh igual a {}'.format(num, hex(num)[2:]))
    else:
        print('Opcao invalida tente novamente')
    
# COMPARANDO NUMEROS
#38 Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor eh maior, Osegundo valor eh maior, nao existe valor maior, os dois sao iguais.

def numeros():
    n1 = int(input('Primeiro numero: '))
    n2 = int(input('Segundo numero: '))
    if n1 > n2:
        print('O primeiro numero eh MAIOR')
    elif n2 > n1:
        print('O segundo numero eh MAIOR')
    else:
        print('Os dois valores sao IGUAIS')

# ALISTAMENTO MILITAR  
# #39 Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao servico militar, se eh hora de se alistar ou se ja passou do tempo do alistamento. Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.

def alistamento():
    from datetime import date
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Voce tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('voce ainda nao tem 18. Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento sera em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Voce ja deveria ter se alistado ha {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
        
# Calculando a Media
#40 Crie um progrmaa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida: Abaixo de 5.0(Reprovado), entre 5.0 e 6.9(Recuperacao) e Acima de 7.0(Aprovado).

def medias():
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1 + n2) / 2
    print('Tirando {:.1f} e {:.1f}, a media do aluno eh {:.1f}'. format(n1, n2, media))
    if 7 > media >= 5:
        print('O aluno esta em recuperacao.')
    elif media < 5:
        print('O aluno esta reprovado.')
    elif media >= 7:
        print('O aluno esta aprovado.')
        
# Classificando Atletas
#41 A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Ate 9 anos(mirim), ate 14 anos(infantil), ate 19 anos(junior), ate 25 anos(senior) e acima de 25 anos(master).

def atletas():
    from datetime import date
    atual = date.today().year
    nascimento = int(input('Ano de nascimento: '))
    idade = atual - nascimento
    print('O atleta tem {} anos'.format(idade))
    if idade <= 9:
        print('Classificao: MIRIM')
    elif idade <= 14:
        print('Classificao: INFANTIL')
    elif idade <= 19:
        print('Classificao : JUNIOR')
    elif idade <= 25:
        print('Classificao: SENIOR')
    else:
        print('Classificao: MASTER')

# Analisando Triangulos v2.0
#42 Refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado: Equilatero, Isosceles e Escaleno.

def triangulo():
    r1 = float(input('Primeiro segmento: '))
    r2 = float(input('Segundo segmento:'))
    r3 = float(input('Terceiro segmento:'))
    if r1 < r2 + r3 and r2 <r1 + r3 and r3 < r1 + r2:
        print('Os segmentos podem formar um triangulo!', end='')
        if r1 == r2 == r3:
            print('Equilatero!')
        elif r1 != r2 != r3 != r1:
            print('Escaleno')
        else:
            print('Isosceles!')
    else:
        print('Os segmentos nao podem formar um triangulo!')
        
# Indice de Massa Corporal
#43 Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela: abaixo de 18.5(Abaixo do Peso), entre 18.5 e 25(Peso ideal), 25 ate 30(Sobrepeso), 30 ate 40(Obesidade) e acima de 40(Obsidade Morbida).

def corporal():
    peso = float(input('Qual eh o seu peso ? (Kg) '))
    altura = float(input('Qual eh sua altura? (m) '))
    imc = peso / (altura ** 2)
    print('O IMC dessa pessoa eh de {:.1f}'.format(imc))
    if imc < 18.5:
        print('Voce esta abaixo do peso normal')
    elif 18.5 <= imc < 25:
        print('Voce esta no peso ideal')
    elif 25 <= imc <30:
        print('Voce esta em sobrepeso')
    elif 30 <= imc < 40:
        print('Voce esta em obesidade')
    else:
        print('Voce esta em obesidade morbida')

# Gerenciador de Pagamentos
#44 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamaneto: a vista dinheiro/cheque(10% de desconto), a vista no cartao(5% de desconto), em ate 2x no cartao(preco normal) e 3x ou mais no cartao (20% de juros).

def gerenciador():
    print('{:^40}'.format('Lojinha'))
    preco = float(input('Preco das Compras: R$'))
    print('''Formas de pagamento
    [ 1 ] a vista dinheiro/cheque
    [ 2 ] a vista no cartao
    [ 3 ] 2x no cartao
    [ 4 ] 3x ou mais no cartao''')
    opcao = int(input('Qual eh a opcao? '))
    if opcao == 1:
        total = preco - (preco * 10 /100)
    elif opcao == 2:
        total = preco - (preco * 5 / 100)
    elif opcao == 3:
        total = preco
        parcela = total / 2
        print('Sua compra sera parcelado em {}x de R$ {:.2f}'.format(parcela))
    elif opcao == 4:
        total = preco + (preco * 20 / 100)
        totparc = int(input('Quantas parcelas?'))
        parcela = total / totparc
        print('Sua compra sera parcela em {}x de R${:.2f}'.format(totparc, parcela))
    else:
        total = preco
        print('Opcao invalida de pagamento.')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
    
# Rock Paper & Scissors
#45 Crie um programa que faca o computador jogar JOKENPO com voce.

def jokenpo():
    from random import randint
    itens = ('Pedra' , 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''Suas opcoes
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('Qual eh a sua jogada? '))
    print('-=' * 12)
    print('Computador jogou {}'.format(itens[computador]))
    print('jogador jogou {}'.format(itens[jogador]))
    print('-=' * 12)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('Jogador Vence')
        elif jogador == 2:
            print('Computador Vence')
        else:
            print('Jogada Invalida')
    elif computador == 1:
        if jogador == 0 :
            print('Computador Vence')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('Jogador Venceu')
        else:
            print('Jogada invalida')
    elif computador == 2:
        if jogador == 0:
            print('Jogador Venceu')
        elif jogador == 1:
            print('Computador Venceu')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('Jogada Invalida')
