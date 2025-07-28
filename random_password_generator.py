import secrets
import string
from datetime import datetime

# ------------------------------
# STEP 1: User Input Function
# ------------------------------
def get_user_inputs():
    """
    Prompt the user for password configuration options and return them as a dictionary.
    Returns:
        dict: A dictionary with keys 'length', 'use_upper', 'use_lower', 'use_digits', 'use_special'.
    """
    print("\n--- Password Configuration ---")
    while True:
        try:    
            length = int(input("Enter desired password length: "))
            if length<=0:
                print("Length must be greater than Zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    if not any([use_upper, use_lower, use_digits, use_special]):
        print("\n[!] At least one character type must be selected. Try again.\n")
        return get_user_inputs()

    return {
        'length': length,
        'use_upper': use_upper,
        'use_lower': use_lower,
        'use_digits': use_digits,
        'use_special': use_special
    }

# --------------------------------------
# STEP 2: Password Generation Function
# --------------------------------------
def generate_secure_password(length, use_upper, use_lower, use_digits, use_special):
    """
    Generate a secure random password using secrets module
    Returns:
        str: The generated password.
    """
    character_sets = []
    mandatory_characters = []

    if use_upper:
        character_sets.append(string.ascii_uppercase)
        mandatory_characters.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        character_sets.append(string.ascii_lowercase)
        mandatory_characters.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        character_sets.append(string.digits)
        mandatory_characters.append(secrets.choice(string.digits))
    if use_special:
        character_sets.append(string.punctuation)
        mandatory_characters.append(secrets.choice(string.punctuation))

    if not character_sets:
        return ""
    
    #Fill remaining lengt with random choices from all selected character sets
    all_characters=''.join(character_sets)
    remaining_length=length-len(mandatory_characters)
    password=mandatory_characters+[secrets.choice(all_characters) for _ in range(remaining_length)]

    #Shuffle to avoid fixed order (Mandatory characters first)
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# --------------------------------------
# STEP 3: Password Strength Checker
# --------------------------------------
def check_password_strength(password):
    """
    Analyze the password and return a strength rating.
    Returns:
        str: 'Weak', 'Moderate', or 'Strong'
    """
    length = len(password)
    score = 0
    feedback = []

    # Points for length
    if length >= 16:
        score+=3
        feedback.append("[✓] Length is excellent (16+)")
    elif length >= 12:
        score+=2
        feedback.append("[✓] Length is good (12–15)")
    elif length >= 8:
        score += 1
        feedback.append("[~] Length is acceptable (8–11)")
    else:
        feedback.append("[✗] Length is too short (<8)")
    
    # Points for character type variety
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if has_upper and has_lower:
        score += 1
        feedback.append("[✓] Has both uppercase and lowercase letters")
    elif has_upper or has_lower:
        feedback.append("[~] Has only one case (upper or lower)")
    else:
        feedback.append("[✗] No letters found")       
    if has_digit:
        score += 1
        feedback.append("[✓] Includes digits")
    else:
        feedback.append("[✗] No digits found")
    if has_special:
        score += 1
        feedback.append("[✓] Includes special characters")
    else:
        feedback.append("[✗] No special characters found")

    # Repetition check
    if len(set(password)) > len(password) * 0.7:
        score += 1
        feedback.append("[✓] Characters are diverse")
    else:
        feedback.append("[✗] Too many repeating characters")
    
    # Patter detection
    common_patterns = ["123", "abc", "qwerty", "password", "111", "000"]
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1
        feedback.append("[✓] No common patterns found")
    else:
         feedback.append("[✗] Contains common patterns (e.g., '123', 'qwerty')")

    # Entropy bonus
    unique_ratio = len(set(password)) / len(password)
    if unique_ratio > 0.8:
        score += 1
        feedback.append("[✓] High entropy (many unique characters)")
    else:
        feedback.append("[~] Could improve character uniqueness")
    
    #Final scoring
    print("\n--- Password Strength Analysis ---")
    for line in feedback:
        print(line)

    print("\nTotal Score:", score, "/ 10")

    if score >= 8:
        return "Strong"
    if score >= 5:
        return "Moderate"
    else:
        return "Weak"

# --------------------------------------
# STEP 4: Save Password to File
# --------------------------------------
def save_password_to_file(password):
    """
    Save the password to a file named 'saved_passwords.txt'.
    """
    password_file='saved_passwords.txt'
    with open(password_file, "a") as file:
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(password + "\n")
    print("\n[+] Password saved to {password_file}.\n")

# --------------------------------------------------
# BONUS: Auto-Generate Inputs (Let Computer Choose)
# --------------------------------------------------
def auto_generate_password():
    """
    Auto-generate configuration settings and return a valid config dictionary.
    """
    length = secrets.randbelow(7) + 12

    while True:
        include_digits = secrets.choice([True, False])
        include_symbols = secrets.choice([True, False])
        include_uppercase = secrets.choice([True, False])
        include_lowercase = secrets.choice([True, False])
        
        if any([include_digits, include_symbols, include_uppercase, include_lowercase]):
            break  # Ensure at least one character type is selected

    print("\nAuto-selected configuration:")
    print(f"Length                     : {length}")
    print(f"Include Uppercase          : {include_uppercase}")
    print(f"Include Lowercase          : {include_lowercase}")
    print(f"Include Digits             : {include_digits}")
    print(f"Include Special Characters : {include_symbols}")

    return {
        'length': length, 
        'use_upper': include_uppercase, 
        'use_lower': include_lowercase, 
        'use_digits': include_digits, 
        'use_special': include_symbols
    }

# ------------------------------
# MAIN MENU LOOP
# ------------------------------
def main():
    print("\n==== Welcome to the Password Generator ====")

    while True:
        print("\n--- Main Menu ---")
        print("1. Generate password (manual inputs)")
        print("2. Check password strength")
        print("3. Auto-generate password (computer chooses)")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            config = get_user_inputs()
            password = generate_secure_password(**config)
            print(f"\nGenerated Password: {password}")
            strength = check_password_strength(password)
            print(f"Password Strength : {strength}")

            if input("\nWould you like to save this password? (y/n): ").lower() == 'y':
                save_password_to_file(password)

        elif choice == '2':
            user_pass = input("\nEnter a password to check strength: ")
            print(f"Strength: {check_password_strength(user_pass)}")

        elif choice == '3':
            config = auto_generate_password()
            password = generate_secure_password(**config)
            print(f"\nAuto-Generated Password: {password}")
            strength = check_password_strength(password)
            print(f"Password Strength        : {strength}")

            if input("\nWould you like to save this password? (y/n): ").lower() == 'y':
                save_password_to_file(password)

        elif choice == '4':
            print("\nThanks for using the Password Generator. Goodbye! \U0001F44B")
            break

        else:
            print("\n[!] Invalid option. Please try again.")


if __name__ == "__main__":
    main()
