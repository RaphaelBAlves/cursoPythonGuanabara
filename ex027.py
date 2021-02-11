nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print(f'Primeiro nome: {dividido[0]}\nÚltimo nome: {dividido[-1]}')