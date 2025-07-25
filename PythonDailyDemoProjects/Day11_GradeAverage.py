# GradeAverage.py
def average_grade(scores):
    avg = sum(scores) / len(scores)
    return avg, "Pass" if avg >= 50 else "Fail"

# Example usage
grades = [float(input(f"Enter score {i+1}: ")) for i in range(5)]
avg, result = average_grade(grades)
print(f"Average: {avg:.2f}, Result: {result}")
