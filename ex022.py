nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')
quantidade_letras = len(nome) - nome.count(' ')
print(f'Quantidade de letras sem contar os espaços: {quantidade_letras}')
nome_dividio = nome.split()
print(f'Quantidade de letras no primeiro nome: {len(nome_dividio[0])}')