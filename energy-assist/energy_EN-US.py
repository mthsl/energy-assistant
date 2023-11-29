print(' ')
print('          _|                      _|            ')
print('_|_|_|        _|    _|    _|_|    _|    _|_|_|  ')
print('_|    _|  _|    _|_|    _|_|_|_|  _|  _|_|      ')
print('_|    _|  _|  _|    _|  _|        _|      _|_|  ')
print('_|_|_|    _|  _|    _|    _|_|_|  _|  _|_|_|    ')
print('_|                                              ')
print('_|')

seeds = {
    1: {'name': 'Popberry', 'energy_cost': 2},
    2: {'name': 'Butterberry', 'energy_cost': 2},
    3: {'name': 'Clover', 'energy_cost': 3.5},
    4: {'name': 'Grainbow', 'energy_cost': 2.5},
    5: {'name': 'Watermint', 'energy_cost': 6.5},
    6: {'name': 'Scarrot', 'energy_cost': 6.5}
}

print(' ')
print('ENERGY CALCULATION SYSTEM: Calculate if it is possible to plant, water, and harvest according to your current energy quantity!')
print(' ')
print('MENU:', ', '.join([f'{key} - {seeds[key]["name"]}' for key in seeds]))
print(' ')

choice = int(input('Enter your choice according to the options above: '))
energy_quantity = float(input('Enter the current energy quantity: '))
seed_quantity = int(input('Enter the quantity of seeds you want to plant: '))

watering_can = 0.5
scissors = 1

if choice in seeds:
    chosen_seed = seeds[choice]
    energy_required = (watering_can + scissors + chosen_seed['energy_cost']) * seed_quantity
    print(f'The energy required to plant, water, and harvest {seed_quantity} {chosen_seed["name"]} is: {energy_required}')
    if energy_quantity < energy_required:
        print(f'Your current energy total is not sufficient to plant {seed_quantity} seeds!')
    else:
        print('Your current energy is sufficient to plant, water, and harvest. Happy farming! :)')

else:
    print('Option not found!')
