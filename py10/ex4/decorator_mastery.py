#!/usr/bin/env python3

from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)


    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise Exception("Spell failed!")

    print("\nTesting retrying spell...")
    print(unstable_spell())

    @power_validator(min_power=10)
    def lightning(power: int) -> str:
        return f"Lightning with {power} power!"

    print("\nTesting power validator...")
    print(f"Power 15: {lightning(15)}")
    print(f"Power 5: {lightning(5)}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(f"Valid name 'Alice': {guild.validate_mage_name('Alice')}")
    print(f"Invalid name 'Bo': {guild.validate_mage_name('Bo')}")
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 5))


if __name__ == "__main__":
    main()
