#!/usr/bin/env python3
import sys
print("=== Command Quest ===")
count = len(sys.argv)
if count == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {count}")

elif count > 1:
    print(f"Program name: {sys.argv[0]}")
    i = 1
    print(f"Argument received: {count - 1}")
    for arg in sys.argv[1:]:
        print(f"Arguments {i}: {arg}")
        i += 1
    print(f"Total arguments: {count}")
