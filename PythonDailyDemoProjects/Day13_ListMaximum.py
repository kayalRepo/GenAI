# ListMaximum.py
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Example usage
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum number is:", find_max(nums))
