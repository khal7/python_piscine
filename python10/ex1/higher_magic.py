from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def amplifier_test(target: str, power: int) -> int:
    return f"{target}: {power}"


def test_condition(target: str, power: int) -> bool:
    return power >= 10


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Arguments must be callable")
    def spell(target, power):
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)
    return spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("Arguments must be callable")
    def spell(target: str, power: int) -> list[tuple]:
        res = base_spell(target, power * multiplier)
        return res
    return spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("Arguments must be callable")
    def new_spell(target: str, power: int):
        res = condition(target, power)
        if res:
            return spell(target, power)
        else:
            return "Spell fizzled"

    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(map(callable, spells)):
        raise TypeError("Arguments must be callable")
    def spell(target: str, power: int):
        my_list = []
        for spel in spells:
            my_list.append(spel(target, power))
        return my_list
    return spell


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combine = spell_combiner(fireball, heal)
    spell1, spell2 = combine("Dragon", 10)
    print(f"Combined spell result: {spell1}, {spell2}")

    print("\nTesting power amplifier...")
    amplifier = power_amplifier(amplifier_test, 3)
    print(f"Original: 10, {amplifier('Amplified', 10)}")

    print("\nTesting conditional caster...")
    condition_test = conditional_caster(test_condition, fireball)
    print(condition_test("the cat", 9))

    print("\nTesting spell sequence...")
    spells = [fireball, heal]
    spell_sequence_test = spell_sequence(spells)
    my_list = spell_sequence_test("Aliens", 10)
    for element in my_list:
        print(element)

