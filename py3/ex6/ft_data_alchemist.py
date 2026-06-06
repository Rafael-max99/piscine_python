#!/usr/bin/python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players = ["Alice", "bob", "Charlie", "dylan",
                       "Emma", "Gregory", "john", "kevin", "Liam"
                       ]

    print(f"Initial list of players: {initial_players}")

    all_capitalized = [
        name.capitalize() for name in initial_players
        ]
    already_capitalized = [
        name for name in initial_players if name == name.capitalize()
        ]
    score_dict = {name: random.randint(0, 1000) for name in all_capitalized}
    average_score = sum(score_dict.values()) / len(score_dict)
    high_scores = {
        name: score for name, score in score_dict.items()
        if score > average_score
        }

    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {already_capitalized}")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(average_score, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
