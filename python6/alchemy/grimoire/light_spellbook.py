

def light_spell_allowed_ingredients() -> list[str]:
    allowed_ingredients = ["earth", "air", "fire", "water"]
    return allowed_ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    if validate_ingredients(ingredients):

        return f"Spell recorded: {spell_name} ({validate_ingredients(ingredients)})"
    else:
        return f"Spell rejected: {spell_name} ({validate_ingredients(ingredients)})"
