

def secure_archive(file_name: str,
                   permission: str = "r",
                   content: str = "") -> tuple[bool, str]:
    if permission == "r":
        try:
            with open(file_name, permission) as file:
                data = file.read()
                return (True, f"{data}")
        except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
            return (False, f"{e}")
    elif permission == "w":
        try:
            with open(file_name, permission) as file:
                file.write(content)
                return (True, "Content successfully written to file")
        except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
            return (False, f"{e}")
    else:
        return (False, "invalid operation")


if __name__ == "__main__":
    content = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n")
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file", "r", content)
    print(result)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/rsyslog.conf", "r", content)
    print(result)

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("txt.txt", "r", content)
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    result = secure_archive("test.txt", "w", content)
    print(result)
