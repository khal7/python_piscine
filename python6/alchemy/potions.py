
import elements as root_level_elements
from alchemy import elements as dir_alchemy_elements


def healing_potion() -> str:
    return (f"Healing potion brewed with "
            f"'{dir_alchemy_elements.create_earth()}'"
            f"and '{dir_alchemy_elements.create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed with "
            f"'{root_level_elements.create_fire()}'"
            f" and '{root_level_elements.create_water()}'")
