
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = 'new_discovery.txt'
    print(f"Initializing new storage unit: {file_name}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    file = open(file_name, 'w')
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 001] New quantum algorithm discovered")

    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 002] Efficiency increased by 347")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    print("[ENTRY 003] Archived by Data Archivist trainee")
    # file.seek(0)
    # file.close()

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")
