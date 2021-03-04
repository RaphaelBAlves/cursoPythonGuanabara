def fatorial(numero=1, mostrar=False):
    """
    Função fatorial tem dois parâmetros.
    O primeiro é o número que se quer o fatorial.
    O segundo é para saber se se deve mostrar o cálculo do fatorial.
    Caso nada seja informado, o parâmetro é False por padrão.

    """

    f = 1
    for n in range(numero, 0, -1):
        f *= n

    if mostrar:
        for n in range(numero, 0, -1):
            if n == 1:
                print(f'{n} = {f}')
            else:
                print(f'{n} x ', end='')

    else:
        print(f'Fatorial de {numero}: {f}')


fatorial(5, True)


