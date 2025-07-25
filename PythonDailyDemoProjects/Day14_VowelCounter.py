# VowelCounter.py
def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

# Example usage
word = input("Enter a word: ")
print("Vowel count:", count_vowels(word))
