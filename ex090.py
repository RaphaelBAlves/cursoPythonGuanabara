dados = {}

dados['Nome'] = input('Nome: ')
dados['Média'] = float(input('Média: '))

if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situaçao'] = 'Reprovado'

for k, v in dados.items():
    print(f'{k} é igual a {v}')
