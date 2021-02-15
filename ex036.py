casa = float(input('Digite o valor da casa que você quer comprar: R$ '))
salario = float(input('Digite o valor do seu salário líquido: R$ '))
anos = int(input('Em quantos anos você quer pagar a casa: '))

teto = (salario * 30) / 100
prestacao = casa / (anos * 12)

if prestacao < teto:
    print('Empréstimo aprovado.')
    print(f'Você vai pagar: R$ {prestacao:.2f} por mês, durante {anos} anos')
else:
    print('Empréstimo negado.')
    print(f'Você teria de pagar: R$ {prestacao:.2f}')
    print('Mas isso vai fazer com que você comprometa mais de 30% do seu salário.')