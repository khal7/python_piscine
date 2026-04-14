import sys 
import os




prefix = sys.prefix
base_prefix = sys.base_prefix
executable_path = sys.executable
venv_name = os.path.basename(prefix)

# print(sys.version_info.major)
# print(sys.version_info.minor)
if prefix == base_prefix:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {prefix}")
    print(f"Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\Scripts\activate # On Windows")
    print("\nThen run this program again.")
else:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {executable_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {prefix}")
    print(f"\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("\nPackage installation path:")
    print(f"{prefix}/lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages")
