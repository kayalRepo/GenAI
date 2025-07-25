# NameList.py
names = [input(f"Enter name {i+1}: ") for i in range(5)]

print("\nNames and their lengths:")
for name in names:
    print(f"{name} - {len(name)} characters")
