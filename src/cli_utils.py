def ask_yes_no(prompt: str) -> bool:
    """
    Prompt the user with a yes/no question.

    Args:
        prompt (str): The question text.

    Returns:
        bool: True if yes, False if no.
    """
    while True:
        ans = input(f"{prompt} (y/n): ").strip().lower()
        if ans in ["y", "yes"]:
            return True
        elif ans in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def ask_int(prompt: str, min_val: int = 1, max_val: int = 128) -> int:
    """
    Prompt user for integer input within a range.

    Args:
        prompt (str): The question text.
        min_val (int): Minimum allowed value.
        max_val (int): Maximum allowed value.

    Returns:
        int: The validated integer input.
    """
    while True:
        try:
            value = int(input(f"{prompt} ({min_val}-{max_val}): "))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
