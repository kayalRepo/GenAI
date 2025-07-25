def format_phone_number(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Check if the number has exactly 10 digits
    if len(num_str) != 10 or not num_str.isdigit():
        return "Invalid input! Please enter a 10-digit number."
    
    # Format as (XXX) XXX-XXXX
    formatted = f"({num_str[:3]}) {num_str[3:6]}-{num_str[6:]}"
    return formatted

# Example usage
phone = input("Enter a 10-digit phone number: ")
print("Formatted number:", format_phone_number(phone))
