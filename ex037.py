numero = int(input('Digite um número: '))
print('Escolha a opção: ')
print('1 - converte para binário')
print('2 - converte para octal')
print('3 - converte para hexadecimal')
opcao = int(input(('Digite: ')))

if opcao == 1:
    print(f'{numero} em binário: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} em octal: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} em hexadecimal: {hex(numero)[2:]}')
else:
    print('Opção inválida.')