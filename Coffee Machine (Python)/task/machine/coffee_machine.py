status = [400, 540, 120, 9, 550]  # water, milk, coffee beans, disposable cups, money
espresso = [250, 0, 16, 1, 4]
latte = [350, 75, 20, 1, 7]
cappuccino = [200, 100, 12, 1, 6]
beverages = [espresso, latte, cappuccino]


def machine_status():
    print('\nThe coffee machine has:')
    print(f'{status[0]} ml of water')
    print(f'{status[1]} ml of milk')
    print(f'{status[2]} g of coffee beans')
    print(f'{status[3]} disposable cups')
    print(f'${(status[4])} of money')


def make_coffee(quantities):
    if status[0] < quantities[0]:
        msg = "Sorry, not enough water!"
    elif status[1] < quantities[1]:
        msg = "Sorry, not enough milk!"
    elif status[2] < quantities[2]:
        msg = "Sorry, not enough coffee beans!"
    elif status[3] < quantities[3]:
        msg = "Sorry, not enough cups!"
    else:
        for i in range(4):
            status[i] -= quantities[i]
        status[4] += quantities[4]
        msg = "I have enough resources, making you a coffee!"
    print(msg)


def buy(beverages):
    coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if coffee_type == "1":
        quantities = beverages[0]  # espresso
        make_coffee(quantities)
    elif coffee_type == "2":
        quantities = beverages[1]  # latte
        make_coffee(quantities)
    elif coffee_type == "3":
        quantities = beverages[2]  # cappuccino
        make_coffee(quantities)
    if coffee_type == "back":
        pass


def fill():
    status[0] += int(input('Write how many ml of water do you want to add:\n> '))
    status[1] += int(input('Write how many ml of milk do you want to add:\n> '))
    status[2] += int(input('Write how many grams of coffee beans do you want to add:\n> '))
    status[3] += int(input('Write how many disposable cups of coffee do you want to add:\n> '))


def take():
    print(f'I gave you ${(status[4])}')
    status[4] -= status[4]


while True:
    action = input('\nWrite action (buy, fill, take, remaining, exit): ')
    if action == 'exit':
        exit()
    elif action == 'buy':
        buy(beverages)
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        machine_status()
