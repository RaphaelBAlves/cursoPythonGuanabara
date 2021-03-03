while True:
    opcao = str(input('Funçao ou biblioteca > ')).strip().lower()

    if opcao == 'fim':
        print('Tchau')
        break
    else:
        help(opcao)
