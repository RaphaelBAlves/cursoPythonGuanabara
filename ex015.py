dias = int(input('Digite os dias: '))
valor_dias = dias * 60
kms = float(input('Digite os KMs rodados: '))
valor_kms = kms * 0.15
valor_total = valor_dias + valor_kms
print('O total a pagar: R$ {:.2f}'.format(valor_total))