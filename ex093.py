dados = {}
gols =[]
total_gols = 0

dados['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))


for p in range(partidas):
    gol = int(input(f'Quantos gols na partida {p + 1}: '))
    total_gols += gol
    gols.append(gol)

dados['gols'] = gols[:]
dados['total'] = total_gols

print(dados)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

for i, j in enumerate(gols):
    print(f'Na partida {i + 1}, fez {j} gols.')

print(f'Um total de {total_gols} gols.')
