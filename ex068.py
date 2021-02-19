from random import randint

vitorias = 0

while True:
    computador = randint(0,10)
    numero = int(input('Digite um número: '))
    soma = computador + numero

    opcao = str(input('Par ou ímpar? [p/i] ')).strip().lower()

    if opcao == 'p' and soma % 2 == 0:
        print(f'Você jogou {numero} e o computador {computador}. Total deu {soma}: PAR')
        print('Você ganhou!')
        print('Vamos jogar novamente...')
        vitorias += 1

    elif opcao == 'i' and soma % 2 != 0:
        print(f'Você jogou {numero} e o computador {computador}. Total deu {soma}: ÍMPAR')
        print('Você ganhou!')
        print('Vamos jogar novamente...')
        vitorias += 1

    elif opcao == 'p' and soma % 2 != 0:
        print(f'Você jogou {numero} e o computador {computador}. Total deu {soma}: ÍMPAR')
        print('Você perdeu.')
        break

    else:
        print(f'Você jogou {numero} e o computador {computador}. Total deu {soma}: PAR')
        print('Você perdeu.')
        break

print(f'Total de vitórias: {vitorias}')
