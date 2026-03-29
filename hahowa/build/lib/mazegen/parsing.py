from typing import Any, Dict


def read_config(path: str) -> Dict[str, str]:
    """Read a config file and return its key-value pairs as strings.

    The function:
    - ignores empty lines and comments
    - checks that each line has the form KEY=VALUE
    - rejects unknown keys
    - rejects duplicate keys

    Args:
        path: Path to the config file.

    Returns:
        A dictionary where each key and value is a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If a line is invalid, a key is unknown,
            or a key appears more than once.
    """
    config = {}
    seen_keys = set()
    allow_keys = [
        "WIDTH", "HEIGHT", "ENTRY",
        "EXIT", "SEED", "OUTPUT_FILE", "PERFECT"]

    with open(path) as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError("Invalid Config File Data!")

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if key not in allow_keys:
                raise ValueError(f"Unknown key: {key}")

            if key in seen_keys:
                raise ValueError(f"Duplicate key: {key}")

            seen_keys.add(key)
            config[key] = value
    return config


def process_value(key: str, value: str) -> Any:
    """Convert one raw config value to the correct Python type.

    The conversion depends on the key:
    - WIDTH and HEIGHT are converted to integers
    - ENTRY and EXIT are converted to tuples of two integers
    - PERFECT is converted to a boolean
    - other values are returned as strings

    Args:
        key: The configuration key name.
        value: The raw string value read from the config file.

    Returns:
        The converted value as int, tuple, bool, or str.

    Raises:
        ValueError: If PERFECT does not contain a valid boolean value.
    """
    if key in ("WIDTH", "HEIGHT", "SEED"):
        return int(value)

    if key in ("ENTRY", "EXIT"):
        parts = value.split(",")
        x = int(parts[0].strip())
        y = int(parts[1].strip())
        return (x, y)

    if key == "PERFECT":
        v = value.strip()

        if v.lower() == "true":
            return True

        if v.lower() == "false":
            return False

        raise ValueError(f"Invalid boolean for PERFECT: {value}")

    return value


def process_config(read_conf: Dict[str, str]) -> Dict[str, Any]:
    """Convert all raw config values to their correct Python types.

    This function goes through each key-value pair in the raw config
    dictionary, applies process_value() to convert the value, and
    stores the result in a new dictionary with lowercase keys.

    Args:
        read_conf: A dictionary containing raw config values as strings.

    Returns:
        A new dictionary containing processed config values.

    Raises:
        ValueError: If one of the config values cannot be processed.
    """
    proccesed_config = {}

    for key, value in read_conf.items():
        try:
            proccesed_config[key.lower()] = process_value(key, value)
        except Exception as e:
            raise ValueError(f"Error in {key}: {value} {e}")

    return proccesed_config


def validate_config(config: Dict[str, Any]) -> None:
    """Validate the processed configuration values.

    This function checks that:
    - WIDTH and HEIGHT are greater than 0
    - ENTRY and EXIT each contain exactly 2 values
    - ENTRY is inside the maze bounds
    - EXIT is inside the maze bounds
    - ENTRY and EXIT are not the same
    - OUTPUT_FILE is not empty

    Args:
        config: A dictionary containing processed config values.

    Raises:
        ValueError: If one or more config values are invalid.
    """
    width = config["width"]
    height = config["height"]
    entry = config["entry"]
    exite = config["exit"]
    output_file = config["output_file"]
    if width <= 0:
        raise ValueError("WIDTH must be greater than 0")
    if height <= 0:
        raise ValueError("HEIGHT must be greater than 0")
    if len(entry) != 2:
        raise ValueError("ENTRY must contain exactly 2 values")
    if len(exite) != 2:
        raise ValueError("EXIT must contain exactly 2 values")
    if not (0 <= entry[0] < width and 0 <= entry[1] < height):
        raise ValueError("ENTRY is outside maze bounds")
    if not (0 <= exite[0] < width and 0 <= exite[1] < height):
        raise ValueError("EXIT is outside maze bounds")
    if entry == exite:
        raise ValueError("ENTRY and EXIT cannot be the same")
    if not output_file:
        raise ValueError("OUTPUT_FILE cannot be empty")
