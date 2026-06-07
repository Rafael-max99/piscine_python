#!/usr/bin/python3

from ex0.factory import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2.strategy import BattleStrategy


def battle(creature1_factory: CreatureFactory, strategy1: BattleStrategy,
           creature2_factory: CreatureFactory, strategy2: BattleStrategy
           ) -> None:

    creature1 = creature1_factory.create_base()
    creature2 = creature2_factory.create_base()

    print("* Battle *")
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("now fight!")

    try:
        strategy1.act(creature1)
    except ValueError as e:
        print(f"Battle error, aborting tournament: {e}")
        return

    try:
        strategy2.act(creature2)
    except ValueError as e:
        print(f"Battle error, aborting tournament: {e}")
        return


def tournament(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]
        ) -> None:

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            battle(factory1, strategy1, factory2, strategy2)


def main() -> None:

    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    defensive_strategy = DefensiveStrategy()
    aggressive_strategy = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy)
    ]
    tournament(opponents)

    print("\n\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy)
    ]
    tournament(opponents)

    print("\n\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy)
    ]
    tournament(opponents)


if __name__ == "__main__":
    main()
