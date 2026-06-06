#!/usr/bin/python3

import random

ACHIEVEMENTS = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable",
        "Boss Slayer", "Strategist", "Unstoppable",
        "Speed Runner", "Survivor", "Treasure Hunter",
        "First Steps", "Sharp Mind"
        ]


def gen_player_achievements() -> set[str]:
    achiv_generator = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, achiv_generator))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    players = {
            "Alice": gen_player_achievements(),
            "Bob": gen_player_achievements(),
            "Charlie": gen_player_achievements(),
            "Dylan": gen_player_achievements()
            }

    for player, achievements in players.items():
        print(f"Player {player}: {achievements}")

    all_achievements: set[str] = set()
    for achievement in players.values():
        all_achievements = all_achievements.union(achievement)
    print(f"\nAll distinct achievements: {all_achievements}")

    values = list(players.values())
    common_achieves: set[str] = set(values[0])
    for achievement in values[1:]:
        common_achieves = common_achieves.intersection(set(achievement))
    print(f"\nCommon achievements: {common_achieves}\n")

    for player, achievements in players.items():
        unique = achievements.copy()
        for other_player, other_achievements in players.items():
            if other_player != player:
                unique = unique.difference(other_achievements)
        print(f"Only {player} has: {unique}")

    print()

    for player, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{player} is missing: {missing}")
