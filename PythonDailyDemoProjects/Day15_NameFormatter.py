# NameFormatter.py
def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) >= 2:
        return f"{parts[-1]}, {' '.join(parts[:-1])}"
    return full_name

# Example usage
name = input("Enter your full name: ")
print("Formatted Name:", format_name(name))
