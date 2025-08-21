from pathlib import Path


def save_password(password: str, filename: str = "passwords.txt") -> None:
    """
    Save password to a text file.

    Args:
        password (str): The password string.
        filename (str): File to save to (default 'passwords.txt').
    """
    path = Path(filename)
    with path.open("a", encoding="utf-8") as f:
        f.write(password + "\n")
