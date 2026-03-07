
print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")
file_name = "classified_data.txt"
with open(file_name, 'r') as file:
    print("SECURE EXTRACTION:")
    print(file.read())

with open('test.txt', 'w+') as f:
    print("\nSECURE PRESERVATION:")
    f.write("[CLASSIFIED] New security protocols archived")
    f.seek(0)

    print(f.read())
    print("Vault automatically sealed upon completion")

print("\nAll vault operations completed with maximum security.")
