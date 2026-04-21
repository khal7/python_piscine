from abc import ABC, abstractmethod
from ex0.creatures import Creature, CreatureFactory


class HealCapability(ABC):
    ...

    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self):
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

# Sproutling is a create has the healing capabilities


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def heal(self) -> str:
        return f"{self.__class__.__name__} heals itself for a small amount"

    def attack(self) -> str:
        return f"{self.__class__.__name__} uses Vine Whip!"


# Bloomelle is a create has the healing capabilities
class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self) -> str:
        return (f"{self.__class__.__name__} heals "
                "itself and others for a large amount")

    def attack(self) -> str:
        return f"{self.__class__.__name__} uses Petal Dance!"

# this creates healing creatures which are the Sproutling and bloomelle


class HealingCreatureFactory(CreatureFactory):
    def __init__(self):
        self.name = "Healing"

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


# Shiftling is a creature that can transfor and revert
class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.transformed:
            return f"{self.__class__.__name__} attacks normally."
        else:
            return f"{self.__class__.__name__} performs a boosted strike!"

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = True
            return f"{self.__class__.__name__} shifts into a sharper form!"
        return f"{self.__class__.__name__} Already Transformed "

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return f"{self.__class__.__name__} returns to normal."
        return f"{self.__class__.__name__} Already revered "


# Shiftling is a creature that can transfor and revert
class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.transformed:
            return f"{self.__class__.__name__} attacks normally."
        else:
            return (f"{self.__class__.__name__} "
                    "unleashes a devastating morph strike!")

    def transform(self) -> str:
        if not self.transformed:
            self.transformed = True
            return (f"{self.__class__.__name__} morphs "
                    "into a dragonic battle form!")
        return f"{self.__class__.__name__} Already transformed "

    def revert(self) -> str:
        if self.transformed:
            self.transformed = False
            return f"{self.__class__.__name__} stabilizes its form."
        return f"{self.__class__.__name__} Already reverted "

# this can create creatures


class TransformCreatureFactory(CreatureFactory):
    def __init__(self):
        self.name = "Transform"

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
