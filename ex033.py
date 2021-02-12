maior = 0
menor = 0

primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))

if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
elif segundo > primeiro and segundo > terceiro:
    maior = segundo
else:
    maior = terceiro

if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
elif segundo < primeiro and segundo < terceiro:
    menor = segundo
else:
    menor = terceiro

print(f'O maior número: {maior}')
print(f'O menor número: {menor}')
