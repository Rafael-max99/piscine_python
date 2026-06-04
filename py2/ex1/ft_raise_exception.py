#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"invalid literal for int() whit base 10: '{temp_str}'")

    if temp <= 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp>= 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp

def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        try:
            print(f"Input data is '{value}'")
            temp = input_temperature(value)
            print(f"Temperature is now {temp}ºC")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
        print()

    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
