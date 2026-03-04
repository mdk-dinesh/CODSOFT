import secrets
import string

def generate_password(length, use_digits=True, use_special=True):
    """Generates a secure random password."""
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    alphabet = letters + digits + special
    
    if not alphabet:
        return ""
    
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    print("--- Secure Password Generator ---")
    
    try:
        length_input = input("Enter the desired password length: ")
        length = int(length_input)
        
        if length <= 0:
            print("Error: Length must be a positive integer.")
            return

        password = generate_password(length)
        
        print("\nGenerated Password:")
        print(f"-------------------")
        print(password)
        print(f"-------------------")
        
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for the length.")

if __name__ == "__main__":
    main()
