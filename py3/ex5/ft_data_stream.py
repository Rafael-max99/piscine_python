#!/usr/bin/python3

import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run", "walk", "grab", "release", "eat",
    "sleep", "climb", "move", "use", "swim"
    ]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while event_list:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen1 = gen_event()
    for num in range(1000):
        player, action = next(gen1)
        print(f"Event {num}: Player {player} did action {action}")

    gen2 = gen_event()
    event_list = []
    for _ in range(10):
        event_list.append(next(gen2))
    print(f"\nBuilt list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
