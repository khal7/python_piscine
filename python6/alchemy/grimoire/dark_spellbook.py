
from .dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed_ingredients = ["bats", "frogs", "arsenic", "eyeball"]
    return allowed_ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:

    if validate_dark_ingredients(ingredients):

        return f"Spell recorded: {spell_name} ({validate_dark_ingredients(ingredients)})"
    else:
        return f"Spell rejected: {spell_name} ({validate_dark_ingredients(ingredients)})"
