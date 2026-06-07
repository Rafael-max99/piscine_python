#!/usr/bin/env python3

from typing import Callable, Any


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


def main() -> None:

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Enemy', 10)}")
    print(f"Amplified: {amplified('Enemy', 10)}")

    print("\nTesting conditional caster...")
    has_mana = lambda t, p: p > 5
    conditional = conditional_caster(has_mana, fireball)
    print(f"With power 10: {conditional('Enemy', 10)}")
    print(f"Whit power 3: {conditional('Enemy', 3)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball, heal])
    results = sequence("Dragon", 20)
    for r in results:
        print(f"{r}")


if __name__ == "__main__":
    main()
