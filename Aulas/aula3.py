n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma eh {}. o produto eh {}, e a divisao eh {:.3f}'.format(s, m, d))
print('Divisao inteira {}, e potencia {}'.format(di, e))