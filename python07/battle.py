from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:

    print("\nTesting factory")
    flame = factory.create_base()
    print(flame.describe())
    print(flame.attack())
    evolved_flame = factory.create_evolved()
    print(evolved_flame.describe())
    print(evolved_flame.attack())
    # print("\n")


def battle(flame_factory: CreatureFactory, aqua_fact: CreatureFactory) -> None:

    print("\nTesting battle")
    flame = flame_factory.create_base()
    aqua = aqua_fact.create_base()
    print(f"{flame.describe()}\n vs.\n{aqua.describe()}\n fight!")
    print(flame.attack())
    print(aqua.attack())


if __name__ == "__main__":
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()

    test_factory(flame_fact)
    # print("\n")
    test_factory(aqua_fact)

    battle(flame_fact, aqua_fact)
