while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        print('Fim do programa')
        break
    else:
        for i in range(11):
            print(f'{numero} X {i} = {numero * i}')
    print('')
    print('-='*10)
