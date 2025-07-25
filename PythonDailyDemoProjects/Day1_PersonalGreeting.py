# Simple Personal Message Script

def main():
    name = input("What is your name? ")
    age = input("How old are you? ")
    color = input("What is your favorite color? ")

    print(f"\nNice to meet you, {name}!")
    print(f"You’re {age} years old and your favorite color is {color}.")
    print(f"{color.capitalize()} is such a lovely color!")

if __name__ == "__main__":
    main()
