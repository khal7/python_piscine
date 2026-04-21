from abc import ABC, abstractmethod
from ex0 import Creature
from ex1.package import HealCapability, TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature):
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def __init__(self):
        self.name = "Normal"

    def act(self, creature: Creature):
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def __init__(self):
        self.name = "Aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy")
        else:
            print(creature.transform())  # type: ignore
            print(creature.attack())
            print(creature.revert())  # type: ignore


class DefensiveStrategy(BattleStrategy):
    def __init__(self):
        self.name = "Defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy")
        else:
            print(creature.attack())
            print(creature.heal())  # type: ignore
