# Condicoes Aninhadas

nome = str(input('Qual eh o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome eh bem popular no Brasil.')
elif nome in 'Ana Claudio Jessica Juliana':
    print('Belo nome feminino')    
else:
    print('Seu nome eh bem normal.')
print('Tenha um bom dia, {}'.format(nome))