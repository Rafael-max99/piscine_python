#!/usr/bin/python3

import typing
import re
from typing import Any, Protocol
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    
    def __init__(self):
        self.data = []
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
            raise ValueError ("Inproper numeric data")

        if isinstance(data, (int, float)):
            self.data.append(str(data))
            self.count += 1
        else: # list
            for val in data:
                self.data.append(str(val))
            self.count += len(data)

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
            raise ValueError ("Inproper text data")

        if isinstance(data, str):
            self.data.append(data)
            self.count += 1
        else: # list
            for val in data:
                self.data.append(val)
            self.count += len(data)

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
            raise ValueError ("Invalid log data")

        if isinstance(data, dict):
            log_str = f"{data.get('log_level', 'UNKNOWN')}: {data.get('log_message', '')}"
            self.data.append(log_str)
            self.count += 1
        else: # list
            for item in data:
                log_str = f"{item.get('log_level', 'UNKNOWN')}: {item.get('log_message', '')}"
                self.data.append(log_str)
            self.count += len(data)

class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class CSVPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = []

        for _, value in data:
            values.append(value)

        csv_row = ",".join(values)
        print(f"CSV Output: {csv_row}")

class JSONPlugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_dict = {}

        for count, value in data:
            json_dict[f"item_{count}"] = value

        print(f"JSON Output: {json_dict}")

class DataStream:

    def __init__(self):
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:

            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data_to_export = []
            item_count = processor.count - len(processor.data)

            for _ in range(nb):
                _, value = processor.output()
                if value:
                    data_to_export.append((item_count, value))
                    item_count += 1

            if data_to_export:
                plugin.process_output(data_to_export)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            proc_name = processor.__class__.__name__
            total = processor.count
            remaining = len(processor.data)
            display_name = re.sub(r'(?<!^)(?=[A-Z])', ' ', proc_name)
            print(f"{display_name}: total {total} items processed, remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    stream = DataStream()
    print("\nInitialize Data Stream...")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
               {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
              42, ['Hi', 'five']]

    print(f"\nSend first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVPlugin())
    stream.print_processors_stats()

    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
			  [{'log_level': 'ERROR', 'log_message': '500 server crash'},
			   {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}],
			  [32, 42, 64, 84, 128, 168], 'World hello']

    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    print("\nSend the same batch again")
    stream.process_stream(batch1)
    stream.print_processors_stats()

if __name__ == "__main__":
    main()



