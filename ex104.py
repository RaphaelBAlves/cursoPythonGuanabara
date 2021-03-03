def leiaint(msg):
    while True:
        numero = input(msg)
        if numero.isdecimal():
            return numero
            break
        else:
            print('Digite um número inteiro.')


n = leiaint('Dgite um número: ')
print(f'Você digitou {n}')