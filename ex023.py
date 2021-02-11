print('-=- Digite um número de 0 a 9999 -=-')
numero = input('Digite um número: ')

if len(numero) == 4:
    print(f'Unidade: {numero[3]}\nDezena: {numero[2]}\nCentena: {numero[1]}\nMilhar: {numero[0]}')
elif len(numero) == 3:
    print(f'Unidade: {numero[2]}\nDezena: {numero[1]}\nCentena: {numero[0]}\nMilhar: 0')
elif len(numero) == 2:
    print(f'Unidade: {numero[1]}\nDezena: {numero[0]}\nCentena: 0\nMilhar: 0')
elif len(numero) == 1:
    print(f'Unidade: {numero[0]}\nDezena: 0 \nCentena: 0\nMilhar: 0')
else:
    print('Leia o enunciado.')