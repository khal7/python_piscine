import sys


def new_fragment(new_file_name: str, content: str) -> None:
    print(f"Saving data to '{new_file_name}'")
    try:
        f = None
        f = open(new_file_name, "w")
        f.write(content)
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{new_file_name}': {e}\n")
        sys.stderr.write("Data not saved\n")

        return
    finally:
        if f:
            f.close()
            print(f"Data saved in file {new_file_name}")


def processing_file(file_name: str) -> None:
    try:
        f = None
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{file_name}'")
        f = open(file_name, "r")
        content = f.read()
        print(f"---\n\n{content}\n---")
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}\n")
        return
    finally:
        if f:
            f.close()
            print(f"File: '{file_name} closed.'\n")

    print("Transform data:")
    content = content.replace("\n", "#\n")
    print(f"---\n\n{content}\n---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file_name = sys.stdin.readline().strip()
    if not new_file_name:
        print("Not saving data.")
    else:
        new_fragment(new_file_name, content)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        processing_file(sys.argv[1])
