import sys


def fun() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id = input("Iput Stream active. Enter archivist ID: ")
    status = input(
        "Input Straem active. Enter status report: ")

    print(
        f"\n[STANDARD] Archive status from {id}: {status}", file=sys.stdout)
    print(f"[ALERT] System diagnostic: {status}",
          file=sys.stderr)
    print("[STANDARD] Data transmisssion complete")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    fun()
