pessoa = {}
lista = []
total_idade = 0
mulheres = []
maior_que_media = []

while True:
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['sexo'] = str(input('Digite o sexo: ')).lower()
    pessoa['idade'] = int(input('Digite a idade: '))
    lista.append(pessoa.copy())
    pergunta = input('Quer continuar? [s/n]: ')
    if pergunta == 'n':
        break

print(f'Pessoas cadastradas: {len(lista)}')

for i in lista:
    for k, v in i.items():
        if k == 'idade':
            total_idade += v
        if k == 'sexo' and v == 'f':
            mulheres.append(i['nome'])

media = total_idade/len(lista)

print(f'Média da idade do grupo: {media:.2f}')
print(f'Lista com mulheres: {mulheres}')

for i in lista:
    for k, v in i.items():
        if k == 'idade':
            if v > media:
                maior_que_media.append(i['nome'])

print(f'Lista com pessoas com idade maior que a média das idades: {maior_que_media}')