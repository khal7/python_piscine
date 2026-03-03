import sys


def current_inventory(ft_dict: dict) -> None:

    pairs = list(ft_dict.items())
    while pairs:
        max_pair = pairs[0]
        for pair in pairs:
            if pair[1] > max_pair[1]:
                max_pair = pair
        percentage = (max_pair[1] / sum(ft_dict.values()) * 100)
        if max_pair[1] == 1:
            print(
                f"{max_pair[0]}, {max_pair[1]} unite ({percentage:.1f}%)")
        else:
            print(
                f"{max_pair[0]}, {max_pair[1]} unites ({percentage:.1f}%)")
        pairs.remove(max_pair)


def inventory_statics(ft_dict) -> None:

    max_value = max(ft_dict.values())
    for key, value in ft_dict.items():
        if value == max_value:
            print(f"Most abundant: {key} ({value} unites)")
            break

    min_value = min(ft_dict.values())
    for key, value, in ft_dict.items():
        if value == min_value:
            print(f"Least abundant: {key} ({value} unit)")
            break


def item_categories(ft_dict: dict) -> None:
    ft_copy = ft_dict.copy()
    max_value = max(ft_dict.values())
    for key, value in ft_copy.items():
        if value == max_value:
            print(f"Moderate: {key, value})")
            del ft_copy[key]
            print(f"Scarce: {ft_copy}")
            break


def restock_needed(ft_dict: dict) -> None:

    restock = []
    for key, value, in ft_dict.items():
        if value == 1:
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
    print(f"Total items in inventory: {sum(my_dict.values())}")
    print(f"Unique item types: {len(my_dict.items())}")

    print(f"\n=== Current Inventory ===")
    current_inventory(my_dict)

    print(f"\n=== Inventory Statistics ===")
    inventory_statics(my_dict)

    print("\n=== Item Categories ===")
    item_categories(my_dict)

    print("\n=== Management Suggestions ===")
    restock_needed(my_dict)

    print("\n=== Dictionary Properties Demo ===")
    dict_proporties(my_dict)
    key = 'sword'
    print(f"Sample lookup - '{key}' in inventory: {key in my_dict}")

    # print(my_dict)


if __name__ == "__main__":
    fun()
