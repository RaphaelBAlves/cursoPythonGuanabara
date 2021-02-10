from math import trunc

num = float(input('Digite um número: '))
parte_inteira = trunc(num)
print('O número {} tem a parte inteira {}'.format(num, parte_inteira))