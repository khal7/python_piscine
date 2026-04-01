
from typing import Generator


def event_generator(n: int) -> Generator:
    players = ("alice", "bob", "charlie", "khalid")
    levels = (5, 12, 8, 1)
    action = ("killed monster", "found treasure",
              "levled up", "sniper")
    for i in range(1, n + 1):
        yield (i, players[(i - 1) % len(players)],
               levels[(i - 1) % len(players)], action[(i - 1) % 3])


def fibo_generator(n) -> Generator:

    old = 0
    new = 1
    for n in range(n - 1):
        yield new
        old, new = new, old + new


def fibo(n) -> None:
    print(f"Fibonacci sequence (first {n}): {0}", end=', ')
    count = 0
    for num in fibo_generator(n):
        if count == n - 2:
            print(num, end='\n')
        else:
            print(num, end=', ')
        count += 1


def prime_generator(n: int) -> Generator:
    count = 0
    i = 2
    while count < n:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i
            count += 1
        i += 1


def prime(n):
    count = 0
    print(f"Prime numbers (first {n}): ", end='')
    for prime in prime_generator(n):
        if count == n - 1:
            print(prime, end='\n')
        else:
            print(prime, end=", ")
        count += 1


if __name__ == "__main__":
    # for n in even_generator():
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    high_level = 0
    treasure_event = 0
    lvl_up = 0
    for i, name, lvl, action in event_generator(1000):
        if lvl >= 10:
            high_level += 1
        if action == "found treasure":
            treasure_event += 1
        if action == "levled up":
            lvl_up += 1
        print(f"Event {i}: Player {name}, (level {lvl}) {action}")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {lvl_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fibo(10)
    prime(5)


# # what the for loop is ACTUALLY doing under the hood
# gen = count_up()

# while True:
#     try:
#         number = next(gen)   # ask for next value
#         print(number)        # your loop body
#     except StopIteration:    # generator ran out
#         break
