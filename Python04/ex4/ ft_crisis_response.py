

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")


file_name = 'lost_archive.txt'
try:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    with open(file_name, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

try:
    print(f"CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    with open('classified_vault.txt', 'r') as file:
        print(file.read())
except PermissionError:
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")

try:
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    with open('standard_archive.txt', 'r') as file:
        print("SUCCESS: Archive recovered - " + file.read())
        print("STATUS: Normal operations resumed")
except Exception as e:
    print(e)

print("\nAll crisis scenarios handled successfully. Archives secure.")
