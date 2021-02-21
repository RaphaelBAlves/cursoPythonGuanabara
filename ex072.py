numeros_escritos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
           'vinte')

numeros_numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

opcao = int(input('Digite um número [0 a 20]: '))

if numeros_numeros.count(opcao) != 0:
    print(f'Número escrito por extenso: {numeros_escritos[opcao]}')
else:
    while numeros_numeros.count(opcao) == 0:
        opcao = int(input('Tente novamente. Digite um número [0 a 20]: '))
    print(f'Número escrito por extenso: {numeros_escritos[opcao]}')


