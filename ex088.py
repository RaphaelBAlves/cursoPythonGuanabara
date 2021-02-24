from random import randint
from time import sleep

mega = []
jogo = []
anterior = 0
quantidade_jogos = int(input('Quantos jogos você quer: '))

for i in range(quantidade_jogos):
    for j in range(6):
        jogo.append(randint(1, 60))
        if j == 0:
            anterior = jogo[j]
        if j > 0:
            if anterior == jogo[j]:
                while anterior == jogo[j]:
                    jogo[j] = randint(1, 60)

        anterior = jogo[j]

    mega.append(jogo[:])
    jogo.clear()

for i, v in enumerate(mega):
    v.sort()
    print(f'Jogo {i + 1}: {v}')
    sleep(1)