import sys


def current_inventory(ft_dict: dict) -> None:
    sum_off_all = sum(ft_dict.values())
    while ft_dict:
        max_key = max(ft_dict, key=ft_dict.get)
        max_value = ft_dict[max_key]
        try:
            percentage = (max_value / sum_off_all) * 100
        except TypeError as e:
            print(e)
        print(
            f"{max_key}: {max_value} unites ({percentage:.1f}%)")
        ft_dict.pop(max_key)


def inventory_statics(ft_dict) -> None:

    max_key = max(ft_dict, key=ft_dict.get)
    max_value = ft_dict[max_key]
    print(f"Most abundant: {max_key} ({max_value} units)")

    max_key = min(ft_dict, key=ft_dict.get)
    max_value = ft_dict[max_key]
    print(f"Least abundant: {max_key} ({max_value} unit)")


def item_categories(ft_dict: dict) -> None:
    categories = {
        'Moderate': {},
        'Scarce': {}
    }
    for item in ft_dict:
        if ft_dict[item] >= 5:
            categories["Moderate"].update({item: ft_dict[item]})
        else:
            categories["Scarce"].update({item: ft_dict[item]})
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")


def restock_needed(ft_dict: dict) -> None:

    restock = []
    for key, value, in ft_dict.items():
        if value <= 1:
            restock.append(key)

    print(f"Restock needed: {', '.join(restock)}")


def dict_proporties(ft_dict: dict) -> None:
    my_keys = []
    my_values = []
    for key, value in ft_dict.items():
        my_keys.append(key)
        my_values.append(str(value))
    print(f"Dictionary keys: {', '.join(my_keys)}")
    print(f"Dictionary values: {', '.join(my_values)}")


def fun() -> None:
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    if len(args) == 0:
        print("No arguments provided!")
        return

    my_dict = {}
    for arg in args:
        splited_arg = arg.split(':')
        try:
            my_dict.update([(splited_arg[0], int(splited_arg[1]))])
        except ValueError as e:
            print(e)
            return
    try:
        print(f"Total items in inventory: {sum(my_dict.values())}")
        print(f"Unique item types: {len(my_dict.items())}")
    except TypeError as e:
        print(e)
        return

    print("\n=== Current Inventory ===")
    my_dict1 = my_dict.copy()
    current_inventory(my_dict1)

    print("\n=== Inventory Statistics ===")
    inventory_statics(my_dict)

    print("\n=== Item Categories ===")
    my_dict2 = my_dict.copy()
    item_categories(my_dict2)

    print("\n=== Management Suggestions ===")
    restock_needed(my_dict)

    print("\n=== Dictionary Properties Demo ===")
    dict_proporties(my_dict)
    key = 'sword'
    print(f"Sample lookup - '{key}' in inventory: {key in my_dict}")


if __name__ == "__main__":
    fun()
