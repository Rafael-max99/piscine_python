#!/usr/bin/python3

import random

def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john", "kevin", "Liam"]

    print(f"Initial list of players: {initial_players}")
    
    already_capitalized = []
    all_capitalized = []

    for name in initial_players:
        if name == name.capitalize():
            already_capitalized.append(name)
        else:
            name = name.capitalize()
        all_capitalized.append(name)
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {already_capitalized}")


    score_dict = {}
    for name in all_capitalized:
        score_dict[name] = random.randint(0, 1000)
    print(f"Score dict: {score_dict}")

    average_score = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average_score, 2)}")

    high_scores = {} 
    for name, score in score_dict.items():
        if score > average_score:
            high_scores[name] = score
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
