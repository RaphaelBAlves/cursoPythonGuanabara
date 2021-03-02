from time import sleep


def contador(inicio=1, fim=10, passo=1):
    for i in range(inicio, fim + 1, passo):
        print(i, end=' ')
        sleep(0.5)

    print()

    for i in range(inicio + 9, fim - 11, -2):
        print(i, end=' ')
        sleep(0.5)

    print()

    inicio = int(input('Digite o início: '))
    fim = int(input('Digite o fim: '))
    passo = int(input('Digite o passo: '))

    if inicio > fim and passo > 0:
        while inicio >= fim:
                print(inicio, end=' ')
                sleep(0.5)
                inicio -= passo

    elif inicio > fim and passo < 0:
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
            sleep(0.5)

    elif inicio > fim and passo == 0:
        for i in range(inicio, fim - 1, -1):
            print(i, end=' ')
            sleep(0.5)

    elif inicio < fim and passo == 0:
        for i in range(inicio, fim + 1, 1):
            print(i, end=' ')
            sleep(0.5)

    elif inicio < fim and passo < 0:
        for i in range(inicio, fim + 1, 1):
            print(i, end=' ')
            sleep(0.5)

    else:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.5)



contador()
