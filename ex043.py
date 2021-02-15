peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    print('Você está abaixo do peso.')
    print(f'IMC: {imc:.1f}')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal.')
    print(f'IMC: {imc:.1f}')
elif imc >= 25 and imc <= 30:
    print('Você está com sobrepeso.')
    print(f'IMC: {imc:.1f}')
elif imc >= 30 and imc <= 40:
    print('Você está com obesidade.')
    print(f'IMC: {imc:.1f}')
else:
    print('Você está com obesidade mórbida.')
    print(f'IMC: {imc:.1f}')