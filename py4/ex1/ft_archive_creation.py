#!/usr/bin/python3

import sys

def read_file(filename: str) -> str | None:
    file = None

    try:
        file = open(filename, "r")
        return file.read()
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': '{e}'")
        return None
    except PermissionError as e:
        print(f"Error opening file '{filename}': '{e}'")
        return None
    except Exception as e:
        print(f"Error opening file '{filename}': '{e}'")
        return None
    finally:
        if file is not None:
            file.close()

def write_file(filename: str, content: str) -> bool:
    file = None

    try:
        file = open(filename, "w")
        file.write(content)
        return True
    except PermissionError as e:
        print(f"Error opening file '{filename}': '{e}'")
        return False
    except Exception as e:
        print(f"Error opening file '{filename}': '{e}'")
        return False
    finally:
        if file is not None:
            file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")

    content = read_file(filename)
    if content is None:
        return

    print("--\n")
    print(content, end="")
    print("\n--")
    print(f"File '{filename}' closed.")

    print("\nTransform data:")

    transformed_lines = []
    lines = content.split("\n")
    for line in lines:
        if line:
            transformed_lines.append(line + "#")
        else:
            transformed_lines.append(line)
    transformed_content = "\n".join(transformed_lines)

    print("--\n")
    print(transformed_content)
    print("--")

    print("\nEnter new file name (or empty):", end=" ")
    new_filename = input()

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    if write_file(new_filename, transformed_content):
        print(f"Data saved in file '{new_filename}'.")
    else:
        print("Data not saved.")

if __name__ == "__main__":
    main()
