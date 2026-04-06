from typing import Any, List, Sequence
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.stack = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        to_be_returned = self.stack[0]
        self.stack.pop(0)
        rank = self.rank
        self.rank += 1
        return (rank, to_be_returned)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.stack = []

    def validate(self, data: Any) -> bool:
        if isinstance(data, int | float):
            return True
        elif isinstance(data, list) and \
                all(isinstance(item, int | float) for item in data):
            return True
        else:
            return False

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self.stack.append(str(item))
            else:
                self.stack.append(str(data))
        else:
            raise TypeError("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.stack = []

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list) and\
                all(isinstance(item, str) for item in data):
            return True
        else:
            return False

    def ingest(self, data: str | List[str]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self.stack.append(item)
            else:
                self.stack.append(data)
        else:
            raise TypeError("Got exception: Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.stack = []

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        elif isinstance(data, list) and \
                all(isinstance(item, dict) for item in data):
            return True
        else:
            return False

    def ingest(self, data: dict | List[dict]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self.stack.append(": ".join(item.values()))
            else:
                self.stack.append(": ".join(data.values()))
        else:
            raise TypeError("Got exception: Improper dict data")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric_processor = NumericProcessor()
    print(
        f"Trying to validate input '42': {numeric_processor.validate(42)}")
    print(
        f"Trying to validate input 'hello':"
        f"{numeric_processor.validate("hello")}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_processor.ingest("foo")
    except TypeError as e:
        print(e)

    data = [1, 2, 3, 4, 5]
    try:
        numeric_processor.ingest(data)
    except TypeError as e:
        print(e)
    print(f"Processing data: {data}")
    extraction_number = 3
    print(f"Extracting {extraction_number} values...")
    for _ in range(extraction_number):
        rank1, data2 = numeric_processor.output()
        print(f"Numeric value {rank1}: {data2}")

    print("\nTesting Text Processor...")
    text_processor = TextProcessor()
    print(f"Trying to validate input '42': {text_processor.validate(42)}")
    data1 = ['Hello', 'Nexus', 'World']
    try:
        text_processor.ingest(data1)
    except TypeError as e:
        print(e)
    print(f"Processing data: {data1}")
    extraction_number = 1
    print(f"Extracting {extraction_number} values...")
    for _ in range(extraction_number):
        rank2, data3 = text_processor.output()
        print(f"Text value {rank2}: {data3}")

    print("\nTesting Log Processor...")
    log_processor = LogProcessor()
    print(
        f"Trying to validate input 'Hello': {log_processor.validate("Hello")}")
    my_list = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {my_list}")
    extraction_number = 2
    print(f"Extracting {extraction_number} values...")
    try:
        log_processor.ingest(my_list)
    except TypeError as e:
        print(e)
    for _ in range(extraction_number):
        rank4, data5 = log_processor.output()
        print(f"Log entry {rank4}: {data5}")
