dados_gerais = []
nome = []
notas = []

while True:
    nome.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    notas.append(media)
    nome.append(notas[:])
    dados_gerais.append(nome[:])
    notas.clear()
    nome.clear()

    pergunta = input('Continuar? [s/n]: ')
    if pergunta == 'n':
        break
print(f'{"No."} {"Nome":<10} {"Média":>20}')
for i, v in enumerate(dados_gerais):
    print(f'{i:<3} {v[0]:.<25} {v[1][2]:.1f}')



while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if opcao == 999:
        break
    print(f'Notas de {dados_gerais[opcao][0]}: {dados_gerais[opcao][1][0]} e {dados_gerais[opcao][1][1]}')