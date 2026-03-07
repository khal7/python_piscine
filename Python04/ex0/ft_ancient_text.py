

def fun() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = 'ancient_fragment.txt'
    print(f"Accessing Storage Vault: {file_name}")
    print("Connection established...\n")

    try:
        print("RECOVERED DATA:")
        file = open(file_name, 'r')
        content = file.read()
        file.close()
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    fun()
