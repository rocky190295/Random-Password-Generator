import secrets
import string


def generate_password(length: int = 12,
                      use_uppercase: bool = True,
                      use_lowercase: bool = True,
                      use_digits: bool = True,
                      use_specials: bool = True) -> str:
    """
    Generate a cryptographically secure random password.

    Args:
        length (int): Desired password length (default 12).
        use_uppercase (bool): Include uppercase A-Z.
        use_lowercase (bool): Include lowercase a-z.
        use_digits (bool): Include digits 0-9.
        use_specials (bool): Include special characters.

    Returns:
        str: Securely generated password.
    """

    # Build the character pool based on user selections
    char_pool = ""
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_specials:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("No character set selected for password generation.")

    # Generate password securely
    password = "".join(secrets.choice(char_pool) for _ in range(length))
    return password
