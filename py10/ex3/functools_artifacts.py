#!/usr/bin/env python3

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul, itemgetter
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str)-> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda a, b: max(a, b), spells)
    elif operation == "min":
        return reduce(lambda a, b: min(a, b), spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable)-> dict[str, Callable]:
    fire_enchant = partial(base_enchantment, power=50, element="fire")
    water_enchant = partial(base_enchantment, power=50, element="water")
    air_enchant = partial(base_enchantment, power=50, element="air")

    return{'fire': fire_enchant, 'water': water_enchant, 'air': air_enchant}


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int)-> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher()-> Callable[[Any], str]:

    @singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"


    @dispatcher.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"


    @dispatcher.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"


    @dispatcher.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatcher


def main() -> None:

    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch({"type": "unknown"}))


if __name__ == "__main__":
    main()
