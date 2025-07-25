# SimplePassword.py
def check_password(password):
    return len(password) >= 8

# Example usage
pw = input("Enter your password: ")
if check_password(pw):
    print("Password is valid")
else:
    print("Password is too short (min 8 characters)")
