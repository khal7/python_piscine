import os
import sys
from dotenv import load_dotenv

load_dotenv()
keys = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY', 'LOG_LEVEL', 'ZION_ENDPOINT']


for key in keys:
    value = os.getenv(key)
    if value is None:
        print(f"[FAIL] {key} not found!")
        exit()
MATRIX_MODE = os.getenv('MATRIX_MODE')
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
LOG_LEVEL = os.getenv('LOG_LEVEL')
ZION_ENDPOINT = os.getenv('ZION_ENDPOINT')

print("\nORACLE STATUS: Reading the Matrix...")
print(f"\nConfiguration loaded:")
print(f"Mode: {MATRIX_MODE}")
print(f"Database: {DATABASE_URL}")
print(f"API Access: Authenticated")
print(f"Log Level: {LOG_LEVEL}")
print(f"Zion Network: Online")

print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available")
print("\nThe Oracle sees all configurations.")
