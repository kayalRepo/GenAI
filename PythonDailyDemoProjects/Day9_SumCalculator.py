# SumCalculator.py
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage
n = int(input("Enter a number: "))
print("Sum from 1 to", n, "is:", sum_to_n(n))
