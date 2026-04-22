
from typing import Callable
from time import time, sleep
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time()
        sleep(0.1)
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if kwargs.get('power', args[0]) >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if _ < max_attempts - 1:
                        print(
                            f"Spell failed, retrying... (attempt {_ + 1}/{max_attempts})")
            else:
                return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@spell_timer
def fireball():
    return "fireball cast!"


@retry_spell(3)
def unstable_spell():
    raise Exception("Spell failed!")


@retry_spell(3)
def stable_spell():
    return "Waaaaaaagh spelled!"


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            return name.replace(" ", "").isalpha()
        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")
    res = fireball()
    print(f"Result: {res}")

    print("Testing retrying spell...")

    print(unstable_spell())
    print(stable_spell())

    print("\nTesting MageGuild...")
    obj = MageGuild()
    res = obj.validate_mage_name("abc")
    res1 = obj.validate_mage_name("ab3c")

    print(res)
    print(res1)

    res2 = obj.cast_spell("Lightning", power=15)
    print(res2)
    res3 = obj.cast_spell("Lightning", power=5)
    print(res3)
