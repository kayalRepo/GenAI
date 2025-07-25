def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

# Example usage
numbers = [10, 15, 22, 33, 42, 57]
check_even_odd(numbers)