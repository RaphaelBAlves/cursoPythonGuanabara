from random import randint

palpite = randint(0,10)
chute = 11
cont = 0

print('-=-=-= Escolha um número de 0 a 10 =-=-=-')
while palpite != chute:
    chute = int(input('Adivinhe o número que o computador pensou: '))
    if chute < palpite:
        print('Mais alto...')
    elif chute > palpite:
        print('Mais baixo...')
    else:
        print(f'Você acertou!\nO computador escolheu: {palpite}\nNúmero de tentativas: {cont}')
    cont += 1


