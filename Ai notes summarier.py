import random
import string

# ---------------- Password Generator ----------------
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# ---------------- Strength Checker ----------------
def check_strength(password):
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    if len(password) >= 8:
        strength += 1

    # Result
    if strength <= 2:
        return "Weak ❌"
    elif strength == 3 or strength == 4:
        return "Medium ⚠️"
    else:
        return "Strong 💪"

# ---------------- MAIN ----------------
print("🔐 Password Generator & Strength Checker")

choice = input("\n1. Generate Password\n2. Check Password Strength\nChoose (1/2): ")

if choice == '1':
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("\nGenerated Password:", password)
    print("Strength:", check_strength(password))

elif choice == '2':
    password = input("Enter your password: ")
    print("Strength:", check_strength(password))

else:
    print("Invalid choice ❌")