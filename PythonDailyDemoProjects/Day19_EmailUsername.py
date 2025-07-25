# EmailUsername.py
def extract_username(email):
    if '@' in email:
        return email.split('@')[0]
    else:
        return "Invalid email address"

# Example usage
email_input = input("Enter an email address: ")
print("Username:", extract_username(email_input))
