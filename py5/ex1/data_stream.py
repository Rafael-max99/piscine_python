#!/usr/bin/python3

import typing
from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    
    def __init__(self) -> None:
        self.data: list[str] = []
        self.count = 0
        self.name: str = ""

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
    
    def __init__(self) -> None:
        super().__init__()
        self.name = "Numeric Processor"

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

    def __init__(self) -> None:
        super().__init__()
        self.name = "Text Processor"

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

    def __init__(self) -> None:
        super().__init__()
        self.name = "Log Processor"

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


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.total_processed: dict[str, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
        self.total_processed[proc.name] = 0

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            processed = False

            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    proc_name = processor.name
                    self.total_processed[proc_name] += 1
                    processed = True
                    break

            if not processed:
                print("DataStream error - Can't process element in stream: "
                    f"{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            proc_name = processor.name
            total = self.total_processed.get(proc_name, 0)
            remaining = len(processor.data)
            print(f"{proc_name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    stream = DataStream()
    print("\nInitialize Data Stream...")
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    stream.register_processor(NumericProcessor())

    batch1 = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
               {'log_level': 'INFO',
                'log_message': 'User wil is connected'}],
              42, ['Hi', 'five']
              ]

    print(f"\nSend first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("\nSend the same batch again")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1"
          )
    for proc in stream.processors:
        if proc.__class__.__name__ == "NumericProcessor":
            for _ in range(3):
                proc.output()
        elif proc.__class__.__name__ == "TextProcessor":
            for _ in range(2):
                proc.output()
        elif proc.__class__.__name__ == "LogProcessor":
            for _ in range(1):
                proc.output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()



