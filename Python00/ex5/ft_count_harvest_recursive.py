def fun(number):
    if (number == 0):
        return
    fun(number - 1)
    print("Day", number)


def ft_count_harvest_recursive():
    get_input = int(input("Days until harvest: "))
    fun(get_input)
    print("Harvest time!")
