def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'

    print(f'Nome do jogador: {nome}')

    print(f'Quantidade de gols de {nome}: {gols}')


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


ficha(nome, gols)