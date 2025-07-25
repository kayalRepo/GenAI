# CountNumbers.py
def count_numbers(numbers):
    positives = sum(1 for n in numbers if n > 0)
    negatives = sum(1 for n in numbers if n < 0)
    zeros = sum(1 for n in numbers if n == 0)
    return positives, negatives, zeros

# Example usage
nums = list(map(int, input("Enter numbers separated by space: ").split()))
pos, neg, zero = count_numbers(nums)
print(f"Positive: {pos}, Negative: {neg}, Zeros: {zero}")
