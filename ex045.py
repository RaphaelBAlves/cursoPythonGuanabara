from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
jogada = str(input('Digite pedra, papel ou tesoura: ')).lower()

escolha_computador = choice(jogadas)

if jogada == escolha_computador:
    print(f'Empate. Você escolheu {jogada} e o computador {escolha_computador}')
elif jogada == 'papel' and escolha_computador == 'pedra':
    print(f'Você ganhou: {jogada} ganha de {escolha_computador}')
elif escolha_computador == 'papel' and jogada == 'pedra':
    print(f'O computador ganhou: {escolha_computador} ganha de {jogada}')
elif jogada == 'pedra' and escolha_computador == 'papel':
    print(f'O computador ganhou: {escolha_computador} ganha de {jogada}')
elif escolha_computador == 'pedra' and jogada == 'papel':
    print(f'Você ganhou: {jogada} ganha de {escolha_computador}')
elif jogada == 'pedra' and escolha_computador == 'tesoura':
    print(f'Você ganhou: {jogada} ganha de {escolha_computador}')
elif escolha_computador == 'pedra' and jogada == 'tesoura':
    print(f'O computador ganhou: {escolha_computador} ganha de {jogada}')
elif jogada == 'tesoura' and escolha_computador == 'pedra':
    print(f'O computador ganhou: {escolha_computador} ganha de {jogada}')
elif escolha_computador == 'tesoura' and jogada == 'pedra':
    print(f'Você ganhou: {jogada} ganha de {escolha_computador}')
elif jogada == 'tesoura' and escolha_computador == 'papel':
    print(f'Você ganhou: {jogada} ganha de {escolha_computador}')
elif escolha_computador == 'tesoura' and jogada == 'papel':
    print(f'O computador ganhou: {escolha_computador} ganha de {jogada}')
elif jogada == 'papel' and escolha_computador == 'tesoura':
    print(f'O computador ganhou: {escolha_computador} ganha de {jogada}')
elif escolha_computador == 'papel' and jogada == 'tesoura':
    print(f'Você ganhou: {jogada} ganha de {escolha_computador}')
else:
    print('Não é possível fazer essa jogada.')



