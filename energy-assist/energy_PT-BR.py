print(' ')
print('          _|                      _|            ')
print('_|_|_|        _|    _|    _|_|    _|    _|_|_|  ')
print('_|    _|  _|    _|_|    _|_|_|_|  _|  _|_|      ')
print('_|    _|  _|  _|    _|  _|        _|      _|_|  ')
print('_|_|_|    _|  _|    _|    _|_|_|  _|  _|_|_|    ')
print('_|                                              ')
print('_|')

seeds = {
    1: {'nome': 'Popberry', 'energia_gasta': 2},
    2: {'nome': 'Butterberry', 'energia_gasta': 2},
    3: {'nome': 'Clover', 'energia_gasta': 3.5},
    4: {'nome': 'Grainbow', 'energia_gasta': 2.5},
    5: {'nome': 'Watermint', 'energia_gasta': 6.5},
    6: {'nome': 'Scarrot', 'energia_gasta': 6.5}
}

print(' ')
print('SISTEMA PARA CÁLCULO DE GASTO DE ENERGIA: Calcule se é possível plantar, regar e colher de acordo com a sua quantidade de energia atual!')
print(' ')
print('MENU:', ', '.join([f'{key} - {seeds[key]["nome"]}' for key in seeds]))
print(' ')

escolha = int(input('Digite sua escolha de acordo com as opções acima: '))
qtd_energia = float(input('Digite a quantidade de energia atual: '))
qtd_seeds = int(input('Digite a quantidade de seeds que deseja plantar: '))

regador = 0.5
tesoura = 1

if escolha in seeds:
    seed = seeds[escolha]
    qtd_energia_gasta = (regador + tesoura + seed['energia_gasta']) * qtd_seeds
    print(f'A quantidade de energia necessária para plantar, regar e colher {qtd_seeds} {seed["nome"]} é de: {qtd_energia_gasta}')
    if qtd_energia < qtd_energia_gasta:
        print(f'Seu total de energia atual não é suficiente para plantar {qtd_seeds} seeds!')
    else:
        print('Sua energia atual é suficiente para plantar, regar e colher. Bom farm! :)')

else:
    print('Opção não encontrada!')
