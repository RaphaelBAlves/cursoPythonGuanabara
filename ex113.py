def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('Erro.')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return numero


def leiafloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('Erro.')
        else:
            return numero


n = leiaint('Digite um número inteiro: ')
print(f'Você digitou {n}')
n = leiafloat('Digite um número real: ')
print(f'Você digitou {n}')