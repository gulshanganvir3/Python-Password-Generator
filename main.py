import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))

    if length < 8:
        print("Password length must be at least 8.")
    else:
        print("Generated password:", generate_password(length))