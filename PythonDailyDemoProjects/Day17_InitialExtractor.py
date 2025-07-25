# InitialExtractor.py
def extract_initials(full_name):
    initials = [part[0].upper() for part in full_name.strip().split() if part]
    return ''.join(initials)

# Example usage
name = input("Enter full name: ")
print("Initials:", extract_initials(name))
