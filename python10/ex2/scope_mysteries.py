from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def call_me():
        nonlocal count
        count += 1
        return count
    return call_me


def spell_accumulator(initial_power: int) -> Callable:

    def accum_power(new_power) -> int:
        nonlocal initial_power
        initial_power += new_power
        return initial_power
    return accum_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(enchant: str):
        return f"{enchantment_type} {enchant}"
    return enchantment

def memory_vault() -> dict[str, Callable]:
    my_dict = {}
    def store(key, value):
        my_dict[key] = value
        
    def recall(key):
        return my_dict.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__=="__main__":
    print("Testing mage counter...")
    mage = mage_counter()
    print(f"counter_a call 1: {mage()}")
    print(f"counter_a call 2: {mage()}")
    mage1 = mage_counter()
    print(f"counter_b call 1: {mage1()}")

    print("\nTesting spell accumulator...")
    accum = spell_accumulator(100)
    print(f"Base 100, add 20: {accum(20)}")
    print(f"Base 100, add 30: {accum(30)}")

    print("\nTesting enchantment factory...")
    echant = enchantment_factory("Flaming")
    echant1 = enchantment_factory("Frozen")
    print(echant("Sword"))
    print(echant1("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    store = vault.get('store')
    recall = vault.get('recall')
    store('secret', 42)
    print(f"Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unkonwn': {recall('unknown')}")



