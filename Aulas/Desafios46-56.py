# Contagem Regressiva
#46 Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles.

def contagem():
    from time import sleep
    for cont in range(10, -1, -1):
        print(cont)
        sleep(1)
    print('Fogos de artificio')

# Contagem de Pares
#47 Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50.

def pares():
    for n in range (2, 51, 2):
        print(n, end=' ')
    print('Acabou')

# Soma impares multiplos de tres.
#48 Faca um progrmaa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no interalo de 1 ate 500.

def tres():
    soma = 0
    cont = 0
    for c in range(1, 501, 2):
        if c % 3 == 0:
            cont = cont + 1
            soma = soma + c
    print('A soma de todos os {} valores solicitados eh {}'.format(cont, soma))

# Tabuada V.2.0
#49 Refaca o DESAFIO 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco FOR.

def tabuada():
    num = int(input('Digite um numero para ver sua tabuada: '))
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num*c))

# Soma dos Pares.
#50 Desenvolva um programa que leia seis numerios inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

def soma():
    soma = 0
    cont = 0
    for c in range(1, 7):
        num = int(input('Digite o {} valor: '.format(c)))
        if num % 2 == 0:
            soma = soma + num
            cont = cont + 1
    print('Voce informou {} numeros e a soma foi {}'.format(cont, soma))

# Progressao Aritmetica
#51 Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.

def aritmetica():
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razao: '))
    decimo = primeiro + (10 - 1) * razao
    for c in range(primeiro, decimo + razao, razao):
        print('{}'.format(c), end=' -> ')
    print('Acabou')
    
# Numeros Primos
#52 Faca um programa que leia um numero inteiro e diga se ele eh ou nao um numero primo.

def primo():
    num = int(input('Digite um numero: '))
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[33m', end='')
            tot += 1 
        else:
            print('\033[31m', end='')
        print('{}'.format(c, end=''))
    print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
    if tot == 2:
        print('E por isso ele eh PRIMO!')
    else:
        print('E por isso ele nao eh PRIMO!')
    
# Detector de Palindromo
#53 Crie um programa que leia uma frase qualqer e diga se ela eh um palindromo, desconsiderando os espacos.

def palindromo():
    frase = str(input('Digite um frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]
    print('O inverso de {} eh {}'.format(junto, inverso))
    if inverso == junto:
        print('Temos um Palindromo!')
    else:
        print('Nao eh um Palindromo')
    
# Grupo da Maioridade
#54 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda atingiram a maioridade e quantas ja sao maiores.

def maioridade():
    from datetime import date
    atual = date.today().year
    totmaior = 0
    totmenor = 0
    for pess in range(1 ,8):
        nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
        idade = atual - nasc
        if idade >= 21:
            totmaior += 1
        else:
            totmenor += 1
    print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
    print('Ao todo tivemos {} pessoas menor de idade'.format(totmenor))

#  Maior e Menor da Sequencia
#55 Faca um programa quie leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

def sequencia():
    maior = 0
    menor = 0
    for p in range(1, 6):
        peso = float(input('Peso da {} pessoa: '.format(p)))
        if peso == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print('O maior peso lido foi de {}Kg'.format(maior))
    print('O menor peso lido foi de {}Kg'.format(menor))

# Analisador Completo
#56Desenvola um programa que leia o nome, idade e sexo de 4 pessoas. No final do preograma, mostre: A media de idade do grupo, Qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
 
def analisador():
    somaidade = 0
    mediaidade = 0
    maioridadehomem = 0
    nomevelho = ''
    totmulher20 = 0
    for p in range(1, 5):
        print('----- {} Pessoa -----'.format(p))
        nome = str(input('Nome: ')).strip()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]: ')).strip()
        somaidade += idade
        if p == 1 and sexo in 'Mm':
            maioridadehomem = idade
            nomevelho = nome
        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
        if sexo in 'Ff' and idade < 20:
            totmulher20 += 1 
            
    mediaidade = somaidade / 4
    print('A media idade do grupo eh de {} anos'.format(mediaidade))
    print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, nomevelho))
    print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))