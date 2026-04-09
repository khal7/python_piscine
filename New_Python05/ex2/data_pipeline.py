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


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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
                    f"DataStream error - Can't process "
                    f"element in stream: {item}")

    def print_processors_stats(self) -> None:
        if not self.workers:
            print("No processor found, no data")
        else:
            for worker in self.workers:
                print(
                    f"{worker}: total {worker.total} items processed,"
                    f"remaining {len(worker.stack)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        all_data = []

        for worker in self.workers:
            for _ in range(nb):
                try:
                    data = worker.output()
                    all_data.append(data)
                except IndexError:
                    break
            plugin.process_output(all_data)
            all_data = []


class CSVPlugin:
    def __init__(self):
        pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values = [value for rank, value in data]
        print(','.join(values))


class JSONPlugin:
    def __init__(self):
        pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        my_dict = {f"item_{rank}": value for rank, value in data}
        print(my_dict)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    print("== DataStream statistics ==")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)
    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING', 'log_message':
               'Telnet access! Use ssh instead'},
              {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
             42, ['Hi', 'five']]
    print(f"\nSend first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVPlugin())
    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()
    other_batch = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                   [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                    {'log_level': 'NOTICE', 'log_message':
                     'Certificateexpires in 10 days'}],
                   [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"\nSend another batch of data: {other_batch}")
    data_stream.process_stream(other_batch)
    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONPlugin())
    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()
