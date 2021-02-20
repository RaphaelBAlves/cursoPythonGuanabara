valor = input('Digite o valor a ser sacado: R$ ')
lista = list(valor)
tamanho = len(lista)

if tamanho == 1:
    unidade = int(lista[0] * 1)

    if unidade == 1:
        print(f'Total de {unidade} cédula de R$ 1')
    elif unidade == 0:
        print(f'Operação inválida.')
    else:
        print(f'Total de {unidade} cédulas de R$ 1')

elif tamanho == 2:
    unidade = int(lista[1] * 1)
    dezena = int(lista[0])

    if dezena % 2 == 0:
        print(f'Total de {dezena / 2:.0f} cédulas de R$ 20 ')
        print(f'Total de {dezena % 2} cédula de R$ 10')
    elif dezena // 2 != 0 :
        print(f'Total de {dezena // 2} cédulas de R$ 20')
        print(f'Total de {dezena % 2 } cédula de R$ 10')
    else:
        print(f'Total de {dezena} cédula de R$ 10')

    if unidade == 1 or unidade == 0:
        print(f'Total de {unidade} cédula de R$ 1')
    else:
        print(f'Total de {unidade} cédulas de R$ 1')

elif tamanho == 3:
    unidade = int(lista[2] * 1)
    dezena = int(lista[1])
    centena = int(lista[0])

    print(f'Total de {centena * 100 / 50:.0f} cédulas de R$ 50')

    if dezena % 2 == 0:
        print(f'Total de {dezena / 2:.0f} cédulas de R$ 20 ')
        print(f'Total de {dezena % 2} cédula de R$ 10')
    elif dezena // 2 != 0 :
        print(f'Total de {dezena // 2} cédulas de R$ 20')
        print(f'Total de {dezena % 2 } cédula de R$ 10')
    else:
        print(f'Total de {dezena} cédula de R$ 10')

    if unidade == 1 or unidade == 0:
        print(f'Total de {unidade} cédula de R$ 1')
    else:
        print(f'Total de {unidade} cédulas de R$ 1')

elif tamanho == 4:
    unidade = int(lista[3] * 1)
    dezena = int(lista[2])
    centena = int(lista[1])
    milhar = int(lista[0])

    print(f'Total de {(centena * 100 / 50) + (milhar * 1000 / 50):.0f} cédulas de R$ 50')

    if dezena % 2 == 0:
        print(f'Total de {dezena / 2:.0f} cédulas de R$ 20 ')
        print(f'Total de {dezena % 2} cédula de R$ 10')
    elif dezena // 2 != 0 :
        print(f'Total de {dezena // 2} cédulas de R$ 20')
        print(f'Total de {dezena % 2 } cédula de R$ 10')
    else:
        print(f'Total de {dezena} cédula de R$ 10')

    if unidade == 1 or unidade == 0:
        print(f'Total de {unidade} cédula de R$ 1')
    else:
        print(f'Total de {unidade} cédulas de R$ 1')

if tamanho > 4:
    print('Só são permitidas operações até R$ 9.999,00')