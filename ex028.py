from random import randrange

resultado = randrange(6)

chute = int(input('Digite um palpite: '))

if chute == resultado:
    print('Você acertou.')
else:
    print(f'Você errou. O computador pensou: {resultado}')