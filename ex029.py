velocidade = float(input('Digite a velocidade: '))

if velocidade > 80:
    print('Você foi multado.')
    print(f'Vai ter que pagar R$ {(velocidade - 80) * 7:.2f}')
else:
    print('Você está na velocidade permitida.')