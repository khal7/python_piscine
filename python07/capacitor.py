from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import Creature


def test_healing_creatures(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def test_transform_creatures(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


if __name__ == "__main__":
    heal_factory = HealingCreatureFactory()

    base_healing_creature = heal_factory.create_base()
    evolved_healing_creature = heal_factory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    test_healing_creatures(base_healing_creature)
    print(" evolved:")
    test_healing_creatures(evolved_healing_creature)

    print("\nTesting Creature with transform capability")
    print(" base:")

    transform_factory = TransformCreatureFactory()

    base_transform_creature = transform_factory.create_base()
    evolved_transform_creature = transform_factory.create_evolved()

    test_transform_creatures(base_transform_creature)
    print(" evolved:")
    test_transform_creatures(evolved_transform_creature)
