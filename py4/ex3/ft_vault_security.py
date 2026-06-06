#!/usr/bin/python3


def secure_archive(
        filename: str, action: int = 0, content: str = ""
        ) -> tuple[bool, str]:
    try:
        if action == 0:
            with open(filename, "r") as file:
                data = file.read()
            return (True, data)
        else:
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file", 0)
    print(result)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/protected_file.txt", 0)
    print(result)

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", 0)
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if result[0]:
        success = secure_archive("new_vault.txt", 1, result[1])
        print(success)


if __name__ == "__main__":
    main()
