seeds = {
    1: {'name': 'Popberry', 'energy_cost': 2},
    2: {'name': 'Butterberry', 'energy_cost': 2},
    3: {'name': 'Clover', 'energy_cost': 3.5},
    4: {'name': 'Grainbow', 'energy_cost': 2.5},
    5: {'name': 'Watermint', 'energy_cost': 6.5},
    6: {'name': 'Scarrot', 'energy_cost': 6.5}
}

print('ENERGY CALCULATION SYSTEM: Check if it is possible to plant, water, and harvest based on your current energy amount!')
print('MENU:', ', '.join(f'{key} - {seed["name"]}' for key, seed in seeds.items()))
print()

choice = int(input('Enter your choice according to the options above: '))
current_energy = float(input('Enter your current energy amount: '))

watering_cost = 0.5
harvesting_cost = 1

def operation_text(operation):
    operations = {1: 'plant', 2: 'water', 3: 'harvest', 4: 'plant and water', 5: 'plant, water, and harvest'}
    return operations.get(operation, 'Option not found!')

if choice in seeds:
    seed = seeds[choice]

    print(' ')
    print('What do you want to do?')
    print('1 - Plant, 2 - Water, 3 - Harvest, 4 - Plant and Water, 5 - Plant, Water, and Harvest')
    print(' ')

    operation_choice = int(input('Enter your choice: '))

    if operation_choice in [1, 2, 3, 4, 5]:
        if operation_choice == 1:
            max_seeds_possible = int(current_energy // seed['energy_cost'])
        elif operation_choice == 2:
            max_seeds_possible = int(current_energy // watering_cost)
        elif operation_choice == 3:
            max_seeds_possible = int(current_energy // harvesting_cost)
        elif operation_choice == 4:
            max_seeds_possible = int(current_energy // (seed['energy_cost'] + watering_cost))
        elif operation_choice == 5:
            max_seeds_possible = int(current_energy // (seed['energy_cost'] + watering_cost + harvesting_cost))
            
        print(f'With the current amount of energy, you can {operation_text(operation_choice)} a maximum of {max_seeds_possible} {seed["name"]}(s).')
    else:
        print('Option not found!')
else:
    print('Option not found!')