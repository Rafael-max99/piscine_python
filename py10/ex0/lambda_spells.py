#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = [m["power"] for m in mages]

    return {
            "max_power": max(powers, key=lambda x: x),
            "min_power": min(powers, key=lambda x: x),
            "avg_power": round(sum(powers) / len(powers), 2)
            }


def main() -> None:
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'artifact'},
        {'name': 'Lightning Rod', 'power': 95, 'type': 'weapon'}
    ]

    mages = [
        {'name': 'Alice', 'power': 80, 'element': 'fire'},
        {'name': 'Bob', 'power': 60, 'element': 'water'},
        {'name': 'Charlie', 'power': 90, 'element': 'air'}
    ]

    spells = ['fireball', 'heal', 'shield']

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) "
          f"comes before {second['name']} ({second['power']} power)")

    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 70)
    print(f"Mages with power >= 70: {[m['name'] for m in strong_mages]}")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
