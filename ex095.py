lista = []
dados = {}
gols =[]
total_gols = 0

while True:
    dados['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))


    for p in range(partidas):
        gol = int(input(f'Quantos gols na partida {p + 1}: '))
        total_gols += gol
        gols.append(gol)

    dados['gols'] = gols[:]
    dados['total'] = total_gols

    lista.append(dados.copy())
    total_gols = 0
    gols.clear()

    pergunta = input('Quer continuar? [s/n]: ')
    if pergunta == 'n':
        break

for i, j in enumerate(lista):
    print(i, end=' ')
    for k in j.values():
        print(f'  {k}  ', end='')
    print('')

print(lista)

while True:
    escolha = int(input('Mostrar dados de qual jogador? '))
    if escolha == 999:
        break
    else:
        if escolha > (len(lista) - 1):
            print('Erro! Não existe jogador com código 5! Tente novamente')
        else:
            for k, v in lista[escolha].items():
                if k == 'nome':
                    print(f'Levantamento do jogador: {v}')
                if k == 'gols':
                    for i, j in enumerate(v):
                        print(f'No jogo {i + 1} fez {j} gols.')

