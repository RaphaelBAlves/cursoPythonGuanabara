print('PRIMEIROS 10 TERMOS DE UMA PA')

primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 1

while cont <= 10:
    if cont == 1:
        print(primeiro_termo, end=' ')
    else:
        primeiro_termo = primeiro_termo + razao
        print(primeiro_termo, end=' ')
    cont += 1