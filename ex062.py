print('PRIMEIROS 10 TERMOS DE UMA PA')

primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
quantidade =1

while cont <= 10:
    if cont == 1:
        print(primeiro_termo, end=' ')
    else:
        primeiro_termo = primeiro_termo + razao
        if cont == 10:
            print(primeiro_termo)
        else:
            print(primeiro_termo, end=' ')
    cont += 1



while quantidade != 0:
    quantidade = int(input('Você quer ver mais quantos termos: '))
    if quantidade != 0:
        for i in range(quantidade):
            primeiro_termo = primeiro_termo + razao
            if i == (quantidade - 1):
                print(primeiro_termo)
            else:
                print(primeiro_termo, end=' ')
