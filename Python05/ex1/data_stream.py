from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self) -> None:
        pass

    def get_stats(self) -> None:
        pass


class SensorStream(DataStream):
    stream_type = "Environmental Data"

    def __init__(self):
        super().__init__()

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing sensor batch: {data_batch}")
        total = 0
        for reading in data_batch:
            try:
                total += reading.get("temp")
            except TypeError as e:
                print(e)

        return f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {total / len(data_batch)}°C"


class TransactionStream(DataStream):
    stream_type = "Financial Data"

    def __init__(self):
        super().__init__()

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing transaction batch: {data_batch}")
        buy = 0
        sell = 0
        for reading in data_batch:
            buy += reading.get("buy", 0)
            sell += reading.get("sell", 0)

        return f"Transaction analysis: {len(data_batch)} operations, net flow: +{buy - sell}units"


class EventStream(DataStream):
    stream_type = "System Events"

    def __init__(self):
        super().__init__()

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing event batch: [{', '.join(data_batch)}]")
        err = 0
        total = 0
        for event in data_batch:
            if event == 'error':
                err += 1
            total += 1
        return f"Event analysis: {total} events, {err} error detected\n"


class StreamProcessor(DataStream):
    pass
