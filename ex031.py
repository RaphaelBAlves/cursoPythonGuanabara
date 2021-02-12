distancia = int(input('Digite a distância em KM: '))

if distancia <= 200:
    passagem = distancia * 0.50
    print(f'Você vai pagar de passagem R$ {passagem:.2f}')
else:
    passagem = distancia * 0.45
    print(f'Você vai pagar de passagem R$ {passagem:.2f}')