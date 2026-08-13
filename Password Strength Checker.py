import string
password = input("Enter your password: ")

errors = []

if len(password) < 8:
    errors.append("Password must be at least 8 characters")

if not any(char.isupper() for char in password):
    errors.append("Add at least one uppercase letter")

if not any(char.islower() for char in password):
    errors.append("Add at least one lowercase letter")

if not any(char.isdigit() for char in password):
    errors.append("Add at least one number")

if not any(char in string.punctuation for char in password):
    errors.append("Add at least one special character")

if not errors:
    print("💪 Strong Password")
else:
    print("⚠️ Weak Password:")
    for error in errors:
        print("-", error)
