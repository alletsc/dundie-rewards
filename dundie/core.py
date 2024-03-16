""" Core module for dundie package."""


def load(filepath):
    """Loads data from a filepath to database."""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"File {filepath} not found.")
