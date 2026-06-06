#!/usr/bin/python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        temp_str = "25"
        print(f"Input data is '{temp_str}'")
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print()

    try:
        temp_str = "abc"
        print(f"Input data is '{temp_str}'")
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}ºC")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
