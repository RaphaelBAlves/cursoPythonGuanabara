produto = float(input('Digite o valor do produto: R$ '))
print('Opções de pagamento: ')
print('1 - à vista dinheiro ou cheque (10% de desconto')
print('2 - à vista no cartão (5% de desconto)')
print('3 - duas vezes no cartão (sem desconto)')
print('4 - três vezes ou mais no cartão (20% de juros)')
opcao = int(input('Escolha opção: '))

if opcao == 1:
    novo_valor = produto - ((produto * 10) / 100)
    print(f'Você vai pagar: R$ {novo_valor:.2f}')
elif opcao == 2:
    novo_valor = produto - ((produto * 5) / 100)
    print(f'Você vai pagar: R$ {novo_valor:.2f}')
elif opcao == 3:
    print(f'Você vai pagar duas parcelas de: R$ {(produto / 2):.2f}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas: '))
    if parcelas >= 3:
        novo_valor = produto + ((produto * 20) / 100)
        print(f'Você vai pagar {parcelas} de: R$ {(novo_valor / parcelas):.2f}')
    else:
        print('Nesta opção, você só pode parcelar a partir de três vezes.')
else:
    print('Opção inválida.')