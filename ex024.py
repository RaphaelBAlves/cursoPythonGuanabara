cidade = str(input('Digite o nome da cidade: ')).strip()
dividir = cidade.split()

if dividir[0].lower() == 'santo':
    print(f'Cidade que você digitou: {cidade}\nEla começa com a palavra: {dividir[0]}')
else:
    print(f'Cidade que você digitou: {cidade}\nEla não começa com a palavra: Santo')
