# NumberComparison.py
def compare_numbers(a, b):
    if a > b:
        return "First number is larger"
    elif a < b:
        return "Second number is larger"
    else:
        return "Both numbers are equal"

# Example usage
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(compare_numbers(a, b))
