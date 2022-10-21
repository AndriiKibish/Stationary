stationery_list = []


def get_item():
    name = input('Enter the name of item (s - stop): ')
    while name != 's':
        price = float(input('Enter price of item: '))
        quantity = int(input('Enter quantity of items: '))
        new_item = name, price, quantity
        stationery_list.insert(0, new_item)
        name = input('Enter the name of item (s - stop): ')
        if name == 's':
            break
    print('Shop is updated')
    print(stationery_list)


while True:
    user_choice = input("Let's fill up the shop: (q - quit) ")
    if user_choice != 'q':
        get_item()
    else:
        print('Process of filling is finished')
        break

