print('PRIMEIROS 10 TERMOS DE UMA PA')

primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))



for i in range(1,11):
    print(primeiro_termo + ((i -1) * razao))