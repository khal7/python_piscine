import sys


def new_fragment(new_file_name: str, content: str) -> None:
    print(f"Saving data to {new_file_name}")
    try:
        f = None
        f = open(new_file_name, "w")
        f.write(content)
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print(f"Error opening file '{new_file_name}': {e}")
        return
    finally:
        if f:
            f.close()
            print(f"Data saved in file {new_file_name}\n")


def processing_file(file_name: str) -> None:
    try:
        f = None
        print("=== Cyber Archives Recovery & Preservation ===")
        f = open(file_name, "r")
        content = f.read()
        print(f"---\n\n{content}\n---")
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    finally:
        if f:
            f.close()
            print(f"File: '{file_name} closed.'\n")

    print("Transform data:")
    content = content.replace("\n", "#\n")
    print(f"---\n\n{content}\n---")
    new_file_name = input("Enter new file name (or empty): ")
    if not new_file_name:
        print("Not saving data.")
    else:
        new_fragment(new_file_name, content)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        processing_file(sys.argv[1])
