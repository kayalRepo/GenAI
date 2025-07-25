def reverse_each_word(sentence):
    # Split the sentence into words, reverse each word, then rejoin with spaces
    return ' '.join([word[::-1] for word in sentence.split()])

def main():
    s = input("Enter a sentence: ")
    result = reverse_each_word(s)
    print("Transformed:", result)

if __name__ == "__main__":
    main()
