from random import randint
from time import sleep

mega = []
jogo = []
anterior = 0
quantidade_jogos = int(input('Quantos jogos você quer: '))

for i in range(quantidade_jogos):
    for j in range(6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break

    mega.append(jogo[:])
    jogo.clear()

for i, v in enumerate(mega):
    v.sort()
    print(f'Jogo {i + 1}: {v}')
    sleep(1)