def aumentar(preco, porcentagem, formatar=True):
    if formatar:
        return moeda(preco + (preco * porcentagem) / 100)
    else:
        return preco + (preco * porcentagem) / 100


def diminuir(preco, porcentagem, formatar=True):

    if formatar:
        return moeda(preco - (preco * porcentagem) / 100)
    else:
        return preco - (preco * porcentagem) / 100


def dobro(preco, formatar=True):
    if formatar:
        return moeda(preco * 2)
    else:
        return preco * 2


def metade(preco, formatar=True):
    if formatar:
        return moeda(preco / 2)
    else:
        return preco / 2


def moeda(preco):
    return f'R$ {preco:.2f}'


def leiadinheiro(msg):
    while True:
        try:
            valor = str(input(msg)).strip().replace(',', '.')
            if valor.isalpha() or valor == '':
                print('Operação inválida.')
            else:
                return float(valor)
        except:
            print('Algo aconteceu de errado.')


def resumo(preco, aumenta, diminui):
    print(f'A metade do preço: {metade(preco)}')
    print(f'O dobro do preço: {dobro(preco)}')
    print(f'Aumento de {aumenta}% sobre o preço: {aumentar(preco, aumenta)}')
    print(f'Redução de {diminui}% sobre o preço: {diminuir(preco, diminui)}')