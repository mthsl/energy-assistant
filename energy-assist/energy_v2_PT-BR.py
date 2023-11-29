seeds = {
    1: {'nome': 'Popberry', 'energia_gasta': 2},
    2: {'nome': 'Butterberry', 'energia_gasta': 2},
    3: {'nome': 'Clover', 'energia_gasta': 3.5},
    4: {'nome': 'Grainbow', 'energia_gasta': 2.5},
    5: {'nome': 'Watermint', 'energia_gasta': 6.5},
    6: {'nome': 'Scarrot', 'energia_gasta': 6.5}
}

print('SISTEMA PARA CÁLCULO DE GASTO DE ENERGIA: Calcule se é possível plantar, regar e colher de acordo com a sua quantidade de energia atual!')
print('MENU:', ', '.join(f'{key} - {seed["nome"]}' for key, seed in seeds.items()))
print()

escolha = int(input('Digite sua escolha de acordo com as opções acima: '))
qtd_energia = float(input('Digite a quantidade de energia atual: '))

regar = 0.5
colher = 1

def operacao_texto(operacao):
    operacoes = {1: 'plantar', 2: 'regar', 3: 'colher', 4: 'plantar e regar', 5: 'plantar, regar e colher'}
    return operacoes.get(operacao, 'Opção não encontrada!')

if escolha in seeds:
    seed = seeds[escolha]

    print(' ')
    print('O que você deseja fazer?')
    print('1 - Plantar, 2 - Regar, 3 - Colher, 4 - Plantar e Regar, 5 - Plantar, Regar e Colher (Todas as ações)')
    print(' ')

    escolha_operacao = int(input('Digite sua escolha: '))

    if escolha_operacao in [1, 2, 3, 4, 5]:
        if escolha_operacao == 1:
            qtd_seeds_possivel = int(qtd_energia // seed['energia_gasta'])
        elif escolha_operacao == 2:
            qtd_seeds_possivel = int(qtd_energia // regar)
        elif escolha_operacao == 3:
            qtd_seeds_possivel = int(qtd_energia // colher)
        elif escolha_operacao == 4:
            qtd_seeds_possivel = int(qtd_energia // (seed['energia_gasta'] + regar))
        elif escolha_operacao == 5:
            qtd_seeds_possivel = int(qtd_energia // (seed['energia_gasta'] + regar + colher))
            
        print(f'Com a quantidade de energia atual, você pode {operacao_texto(escolha_operacao)} no máximo {qtd_seeds_possivel} {seed["nome"]}(s).')
    else:
        print('Opção não encontrada!')
else:
    print('Opção não encontrada!')
