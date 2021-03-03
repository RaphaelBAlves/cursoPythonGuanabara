def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'

    print(f'Nome do jogador: {nome}')

    if gols == '':
        gols = 0

    print(f'Quantidade de gols de {nome}: {gols}')


nome = input('Nome do jogador: ')
gols = input('Gols: ')

ficha(nome, gols)