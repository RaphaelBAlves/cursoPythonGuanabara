reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 < reta2 + reta3 and reta1 > abs(reta2-reta3):
    if reta2 < reta1 + reta3 and reta2 > abs(reta1 - reta3):
        if reta3 < reta1 + reta2 and reta3 > abs(reta1 - reta2):
            print(f'As retas {reta1}, {reta2}, {reta3} podem formar um triângulo.')
            if reta1 == reta2 and reta2 == reta3:
                print('O retângulo é equilátero.')
            elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
                print('O retângulo é isósceles.')
            else:
                print('O retângulo é escaleno.')
else:
    print(f'As retas {reta1}, {reta2}, {reta3} não podem formar um triângulo')