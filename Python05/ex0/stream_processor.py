

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self):
        pass

    def process(self, data: Any) -> str:
        return f"Processed {len(data)} numeric values,"
        f"sum={sum(data)}, avg={sum(data) / len(data)}"

    def validate(self, data: any) -> bool:
        for n in data:
            if type(n) is not int:
                return False
        return True


class TextProcessor(DataProcessor):
    def __init__(self):
        pass

    def process(self, data: Any) -> str:
        return f"Proccessed text: {len(data)}"
        f"characters, {len(data.split())} words"

    def validate(self, data: any) -> bool:
        if type(data) is str:
            return True
        return False


class LogProcessor(DataProcessor):
    def __init__(self):
        pass

    def process(self, data: Any) -> str:
        if "ERROR" in data:
            return "[ALERT] ERROR level detected: Connection timeout"
        elif "[INFO]" in data:
            return "[INFO] INFO level detected: System ready"

    def validate(self, data: any) -> bool:
        if type(data) is str:
            return True
        return False


print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

print("Initializing Numeric Processor...")
num_data = [1, 2, 3, 4, 5]
print(f"Processing data: {num_data}")
num_processor = NumericProcessor()
if num_processor.validate(num_data):
    print("Validation: Numeric data verified")
else:
    print("validation failed: invalid data")
res = num_processor.process(num_data)
print(num_processor.format_output(res))


print("\nInitializing Text Processor...")
text_data = "Hello Nexus World"
text_processor = TextProcessor()
print(f"Processing data: {text_data}")
if text_processor.validate(text_data):
    print("Validation: Text data verified")
else:
    print("Validation failed: invalid data")
res1 = text_processor.process(text_data)
print(text_processor.format_output(res1))


print("\nInitializing Log Processor...")
log_processor = LogProcessor()
data = "ERROR: Connection timeout"
print(f"Processing data: {data}")
if log_processor.validate(data):
    print("Validation: Log entry verified")
else:
    print("validation failed: invalid data")
res = log_processor.process(data)
print(log_processor.format_output(res))


print("\n=== Polymorphic Processing Demo ===")
print("Processing multiple data types through same interface...")
num = [2, 2, 2]
num_pro = NumericProcessor()
print(f"Result 1: {num_pro.process(num)}")
txt = "hello world!"
txt_pro = TextProcessor()
print(f"Resutl 2: {txt_pro.process(txt)}")
log_pro = LogProcessor()
log = "[INFO]"
print(f"Result 3: {log_pro.process(log)}")

print("\nFoundation systems online. Nexus ready for advanced streams.")
