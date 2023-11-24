#22 Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiusculas e minusculas, quantas letras ao todo(sem considerar os espacos) e quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiuscula eh {}'.format(nome.upper()))
print('seu nome em minuscula eh {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome eh {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#23 Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#24 Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO".

cid = str(input('Em qual cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

#25 Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual eh o seu nome completo? ')).strip()
print('Seu nome tem Silva {}'.format('SILVA' in nome.upper()))

#26 Faca um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A", em que posicao ela aparece a primeira vez e em que posicao ela aparece a ultima vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))

#27 Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome eh {}'.format(nome[0]))
print('Seu ultimo nome eh {}'.format(nome[len(nome)-1]))