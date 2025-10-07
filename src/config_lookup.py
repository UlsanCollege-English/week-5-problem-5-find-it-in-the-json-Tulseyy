
# src/config_lookup.py

def find_key(data, key):
    """
    Depth-first left-to-right search for the first occurrence of key.
    Return value or None if not found.
    """
    if isinstance(data, dict):
        # If key exists at this level, return immediately
        if key in data:
            return data[key]

        # Otherwise, search recursively in each value
        for value in data.values():
            result = find_key(value, key)
            if result is not None:
                return result

    elif isinstance(data, (list, tuple)):
        # Search recursively in each element of the sequence (lists and tuples)
        for item in data:
            result = find_key(item, key)
            if result is not None:
                return result

    # Key not found
    return None


# Example usage / test
if __name__ == "__main__":
    config = {
        "database": {
            "user": "admin",
            "settings": {
                "timeout": 30,
                "retries": 3
            }
        },
        "services": [
            {"name": "auth", "enabled": True},
            {"name": "cache", "settings": {"size": "2GB"}},
        ]
    }

    print(find_key(config, "timeout"))   # Output: 30
    print(find_key(config, "size"))      # Output: "2GB"
    print(find_key(config, "missing"))   # Output: None
