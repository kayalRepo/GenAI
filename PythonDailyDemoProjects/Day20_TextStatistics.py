# TextStatistics.py
def text_statistics(paragraph):
    words = paragraph.split()
    sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
    characters = len(paragraph)

    return len(words), sentences, characters

# Example usage
text = input("Enter a paragraph: ")
word_count, sentence_count, char_count = text_statistics(text)

print(f"Words: {word_count}")
print(f"Sentences: {sentence_count}")
print(f"Characters: {char_count}")
