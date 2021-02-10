from math import cos, sin, tan, radians

num = int(input('Digite um ângulo: '))
print('O seno: {:.2f}'.format(sin(radians(num))))
print('O cosseno: {:.2f}'.format(cos(radians(num))))
print('A tangente: {:.2f}'.format(tan(radians(num))))