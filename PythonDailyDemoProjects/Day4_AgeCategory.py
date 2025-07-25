# AgeCategory.py
def age_category(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Example usage
age = int(input("Enter age: "))
print("Category:", age_category(age))
