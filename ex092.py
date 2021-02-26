from datetime import datetime

dados = {}

dados['nome'] = input('Nome: ')
ano_nascimeto = int(input('Ano nascimento: '))
ano_atual = datetime.today().year
idade = ano_atual - ano_nascimeto
dados['idade'] = idade
while True:
    ctps = int(input('CTPS (0 não tem): '))
    if ctps == 0:
        dados['ctps'] = 0
        break
    else:
        dados['ctps'] = ctps
        break
if dados['ctps'] == 0:
    print('Você não tem carteira de trabalho. Não dá para calcular o ano que você vai se aposentar.')
else:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))

    aposentadoria = idade + (35 - (ano_atual - dados['contratacao']))
    dados['aposentadoria'] = aposentadoria

    for k, v in dados.items():
        print(f'{k} tem o valor {v}')