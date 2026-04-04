import sys

if len(sys.argv) == 1:
    print("Usage: ft_ancient_text.py <file>")

else:
    file_name = sys.argv[1]
    try:
        f = None
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{file_name}'")
        f = open(file_name, "r")
        content = f.read()
        print(f"---\n\n{content}\n\n---")
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        print(f"Error opening file '{file_name}': {e}")
    finally:
        if f:
            f.close()
            print(f"File: '{file_name} closed.'")

    # permission file: /etc/rsyslog.conf
