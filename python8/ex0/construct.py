import sys
import os

# current python environment
prefix = sys.prefix

# always means the global python installs
# regardless of you run script in venv or not
base_prefix = sys.base_prefix

# full path of python currently running your script
# so output depend on from where you run the script
executable_path = sys.executable

# extract the last parm of prefix so in returns the name of the venv
venv_name = os.path.basename(prefix)


if prefix == base_prefix:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {executable_path}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("\nThen run this program again.")
else:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {executable_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("\nPackage installation path:")
    print(f"{prefix}/lib/python{sys.version_info.major}."
          f"{sys.version_info.minor}/site-packages")
