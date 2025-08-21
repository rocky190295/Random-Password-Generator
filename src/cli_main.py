import argparse
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("No character types selected.")

    return ''.join(random.choice(char_pool) for _ in range(length))

def save_password(password, path="data/saved_passwords.txt"):
    with open(path, "a") as f:
        f.write(password + "\n")

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
    parser.add_argument("--upper", action="store_true", help="Include uppercase letters")
    parser.add_argument("--lower", action="store_true", help="Include lowercase letters")
    parser.add_argument("--digits", action="store_true", help="Include digits")
    parser.add_argument("--symbols", action="store_true", help="Include symbols")
    parser.add_argument("--save", action="store_true", help="Save password to file")

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.upper, args.lower, args.digits, args.symbols)
        print("Generated Password:", password)
        if args.save:
            save_password(password)
            print("Password saved to file.")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()