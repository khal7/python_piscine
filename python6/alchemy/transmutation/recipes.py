from .. import elements, potions
import elements as root_level_elements


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{elements.create_air()}' and '{potions.strength_potion()}' mixed with '{root_level_elements.create_fire()}'"


if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        f"Testing lead to gold: {lead_to_gold()}")
