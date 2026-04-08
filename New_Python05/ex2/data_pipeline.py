from typing import Any, List, Sequence, Protocol
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
                    f"DataStream error - Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        if not self.workers:
            print("No processor found, no data")
        else:
            for worker in self.workers:
                print(
                    f"{worker}: total {worker.total} items processed, remaining {len(worker.stack)} on processor")


class ExportPlugin(Protocol):
    ...


class CVSPlugin:
    ...


class JSONPlugin:
    ...
