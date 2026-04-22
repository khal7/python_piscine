from functools import reduce, partial, wraps, lru_cache, singledispatch
from typing import Callable, Any
from operator import add, mul


def base_enchant(power: int, element: str, target: str) -> str:
    return f"The {target} has {power} of power, {element} element"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    elif operation == "add":
        result = reduce(add, spells)
    elif operation == "multiply":
        result = reduce(mul, spells)
    elif operation == "max":
        result = reduce(max, spells)
    elif operation == "min":
        result = reduce(min, spells)
    else:
        raise ValueError("unknown operation!")
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    specialized1 = partial(base_enchantment, 50, "Fire")
    specialized2 = partial(base_enchantment, 50, "Lightning")
    specialized3 = partial(base_enchantment, 50, "Ice")
    return {"fire": specialized1, "lightning": specialized2, "ice": specialized3}


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(target: Any):
        return "Unknown spell type"

    @spell.register(int)
    def _(target: int):
        return f"Damage spell: {target} damage"

    @spell.register(str)
    def _(target: str):
        return f"Enchantment: {target}"

    @spell.register(list)
    def _(target: list):
        return f"Multi-cast: {len(target)} spells"
    return spell
    
if __name__ == "__main__":
    print("\nTesting spell reducer...")
    my_list = [10, 20, 30, 40]
    try:
        result_sum = spell_reducer(my_list, "add")
        print(f"Sum: {result_sum}")

        result_product = spell_reducer(my_list, "multiply")
        print(f"Product: {result_product}")

        result_max = spell_reducer(my_list, "max")
        print(f"max: {result_max}")
    except ValueError as e:
        print(e)

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()

    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher(1.2))

    
