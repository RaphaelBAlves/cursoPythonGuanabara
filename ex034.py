salario = float(input('Digite o salário: '))

if salario > 1250:
    novo_salario = salario + ((salario * 10) / 100)
    print(f'Novo salário, com 10% a mais: R$ {novo_salario}')
else:
    novo_salario = salario + ((salario * 15) / 100)
    print(f'Novo salário, com 15% a mais: R$ {novo_salario}')
