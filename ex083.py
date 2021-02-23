parenteses_aberto = '('
parenteses_fechado = ')'
cont_aberto = 0
cont_fechado = 0


expressao = input('Digite uma expressão matemática: ')
lista = list(expressao)

for i in lista:
    if i == parenteses_aberto:
        cont_aberto += 1

    if i == parenteses_fechado:
        cont_fechado += 1

if cont_aberto == cont_fechado:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
