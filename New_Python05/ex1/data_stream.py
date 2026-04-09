from typing import Any, List, Sequence
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.stack = []
        self.rank = 0
        self.total = 0

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

    def __str__(self):
        return "Numeric Processor"

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
                    self.total += 1
            else:
                self.stack.append(str(data))
                self.total += 1
        else:
            raise TypeError("Got exception: Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.stack = []

    def __str__(self):
        return "Text Processor"

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
                    self.total += 1
            else:
                self.stack.append(data)
                self.total += 1
        else:
            raise TypeError("Got exception: Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.stack = []

    def __str__(self):
        return "Log Processor"

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
                    self.total += 1
            else:
                self.stack.append(": ".join(data.values()))
                self.total += 1
        else:
            raise TypeError("Got exception: Improper dict data")


class DataStream():
    def __init__(self):
        self.workers = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.workers.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            flag = False
            for worker in self.workers:
                if worker.validate(item):
                    worker.ingest(item)
                    flag = True
                    break
            if not flag:
                print(
                    f"DataStream error - Can't process"
                    f"element in stream: {item}")

    def print_processors_stats(self) -> None:
        if not self.workers:
            print("No processor found, no data")
        else:
            for worker in self.workers:
                print(
                    f"{worker}: total {worker.total} items \
                    processed, remaining {len(worker.stack)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)
    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING', 'log_message':
               'Telnet access! Use ssh instead'}, {
                 'log_level': 'INFO', 'log_message': 'User wil is connected'}],
             42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {batch}")
    data_stream.process_stream(batch)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print("\nRegistering other data processors")
    print("Send the same batch again")
    text = TextProcessor()
    log = LogProcessor()
    data_stream.register_processor(text)
    data_stream.register_processor(log)
    data_stream.process_stream(batch)
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
