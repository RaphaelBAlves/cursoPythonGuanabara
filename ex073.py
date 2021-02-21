times = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't')

print(f'Primeiros cinco colocados: {times[:5]}')
print(f'Quatro últimos colocados: {times[-4:]}')
print(f'Lista em ordem alfabética: {sorted(times)}')
print(f'O time "c" está na posição {(times.index("c") + 1)} da tabela')