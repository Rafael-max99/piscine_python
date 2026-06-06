#!/usr/bin/python3

import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    filename = sys.argv[1]
    print(f"Accessing file '{filename}'", end="")

    try:
        file: IO[str] = open(filename, "r")
        print("--")
        content = file.read()
        file.close()
        print(content, end="")
        print("--")
        print(f"File '{filename}' closed.")
    except FileNotFoundError as e:
        print()
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print()
        print(f"Error opening file '{filename}': {e}")
    except Exception as e:
        print()
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
