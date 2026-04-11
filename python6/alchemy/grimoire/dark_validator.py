
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    ingredient_list = light_spell_allowed_ingredients()
    if any(item in ingredients.lower() for item in ingredient_list):
        return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")
