#!/usr/bin/python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[str] = []
        self.count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if self.data:
            data = self.data.pop(0)
            return (self.count, data)
        return (self.count, "")


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            for val in data:
                if not isinstance(val, (int, float)):
                    return False
            return True

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, (int, float)):
            self.data.append(str(data))
        else: # list
            for val in data:
                self.data.append(str(val))

        self.count += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            for val in data:
                if not isinstance(val, str):
                    return False
            return True

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self.data.append(data)
        else: # list
            for val in data:
                self.data.append(val)

        self.count += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True

        if isinstance(data, list):
            for val in data:
                if not isinstance(val, dict):
                    return False
                for key, value in val.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid log data")

        if isinstance(data, dict):
            level = data.get('log_level', 'UNKNOWN')
            msg = data.get('log_message', '')
            log_str = f"{level}: {msg}"
            self.data.append(log_str)
        else: # list
            for item in data:
                level = item.get('log_level', 'UNKNOWN')
                msg = item.get('log_message', '')
                log_str = f"{level}: {msg}"
                self.data.append(log_str)

        self.count += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input: '42': {numeric.validate(42)}")
    print(f"Trying to validate input: 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")

    numeric.ingest([1, 2, 3, 4, 5])
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Extracting 3 values...")
    for i in range(3):
        count, value = numeric.output()
        print(f"Numeric value {i}: {value}")

    # test TextProcessor
    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Processing data: ['Hello', 'Nexus', 'World']")
    print("Extracting 1 value...")
    count, value = text.output()
    print(f"Text value 0: {value}")

    # test LogProcessor
    print("\n\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    log_data = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
            ]
    log.ingest(log_data)
    print(f"Processing data: {log_data}")
    print("Extracting 2 values...")
    for i in range(2):
        count, value = log.output()
        print(f"Log entry {i}: {value}")


if __name__ == "__main__":
    main()



