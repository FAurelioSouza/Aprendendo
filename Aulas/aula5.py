'''nome = str(input('Qual eh o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo voce tem!')
else:
    print('Que nomezinho padrao!')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(m))
if m>= 6.0:
    print('Sua media foi boa! Parabens')
else:
    print('Sua media foi ruim! Estuda ai!')