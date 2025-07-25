# SimpleCipher.py
def simple_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift character by 1
            if char.lower() == 'z':
                shifted = 'a'
            else:
                shifted = chr(ord(char.lower()) + 1)
            result += shifted
        else:
            result += char
    return result

# Example usage
input_text = input("Enter a word: ")
print("Ciphered text:", simple_cipher(input_text))
