numero = 0

while numero != 5:
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro: '))

    print('Opções:')
    print('[1] - somar')
    print('[2] - multiplicar')
    print('[3] - maior')
    print('[4] - novos números')
    print('[5] - sair do programa')
    opcao = int(input('Escolha: '))

    if opcao == 1:
        soma = numero1 + numero2
        print(f'Soma: {soma:.2f}')
    elif opcao == 2:
        multiplicar = numero1 * numero2
        print(f'Multiplicação: {multiplicar:.2f}')
    elif opcao == 3:
        if numero1 > numero2:
            print(f'O número maior: {numero1}')
        else:
            print(f'O número maior: {numero2}')
    elif opcao == 5:
        numero  = 5

print('Fim do programa')