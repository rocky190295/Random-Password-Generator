import math
import string


def calculate_entropy(password: str, char_pool_size: int) -> float:
    """
    Estimate password entropy in bits.

    Args:
        password (str): The password string.
        char_pool_size (int): Size of the character pool used.

    Returns:
        float: Estimated entropy (bits).
    """
    if not password:
        return 0.0
    return math.log2(char_pool_size ** len(password))


def check_strength(password: str) -> dict:
    """
    Analyze the strength of a password.

    Args:
        password (str): Password string.

    Returns:
        dict: Analysis with length, character variety, repetition,
              entropy, and verdict.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    # Determine pool size
    pool_size = 0
    if has_upper:
        pool_size += len(string.ascii_uppercase)
    if has_lower:
        pool_size += len(string.ascii_lowercase)
    if has_digit:
        pool_size += len(string.digits)
    if has_special:
        pool_size += len(string.punctuation)

    entropy = calculate_entropy(password, pool_size)

    verdict = "Weak"
    if entropy >= 80:
        verdict = "Strong"
    elif entropy >= 60:
        verdict = "Moderate"

    return {
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "entropy_bits": round(entropy, 2),
        "verdict": verdict
    }
