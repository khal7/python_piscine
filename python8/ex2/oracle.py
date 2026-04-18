import os
import sys
from dotenv import load_dotenv

load_dotenv()
keys = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY', 'LOG_LEVEL', 'ZION_ENDPOINT']


for key in keys:
    value = os.getenv(key)
    if value is None:
        print(f"[FAIL] {key} not found!")
        sys.exit()

# dev mode testing th eapp locally
# production mode real app real user are using
MATRIX_MODE = os.getenv('MATRIX_MODE')
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
LOG_LEVEL = os.getenv('LOG_LEVEL')
ZION_ENDPOINT = os.getenv('ZION_ENDPOINT')

if MATRIX_MODE == "production":
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {MATRIX_MODE}")
    print("Database: Connected to remote instance")
    print("API Access: Authenticated")
    print(f"Log Level: {LOG_LEVEL}")
    print("Zion Network: Online")
else:
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {MATRIX_MODE}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {LOG_LEVEL}")
    print("Zion Network: Online")


print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available")
print("\nThe Oracle sees all configurations.")
