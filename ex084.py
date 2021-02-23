pessoas = []
dados = []
pessoas_pesadas =[]
pessoas_leves = []
maior_peso = 0
menor_peso = 0

while True:
    dados.append(input('Digite nome: '))
    dados.append(float(input('Digite peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    pergunta = input('Quer adicionar mais dados? [s/n]: ')
    if pergunta == 'n':
        break

for p in pessoas:
    if p[1] > maior_peso:
        maior_peso = p[1]

    if p == pessoas[0]:
        menor_peso = 0

    if p[1] < menor_peso:
        menor_peso = p[1]

for p in pessoas:
    if p[1] >= maior_peso:
        pessoas_pesadas.append(p[0])
    if p[1] <= menor_peso:
        pessoas_leves.append(p[0])


print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'Maior peso foi {maior_peso} kg: Os mais pesados: {pessoas_pesadas}')
print(f'Maior peso foi {menor_peso} kg: Os mais pesados: {pessoas_leves}')
