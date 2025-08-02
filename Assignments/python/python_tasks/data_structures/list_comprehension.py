# List comprehension for words with odd number of characters
words = ["apple", "banana", "kiwi", "grape", "orange", "fig", "pear"]
odd_length_words = [word for word in words if len(word) % 2 == 1]
print(f"Words with odd number of characters: {odd_length_words}")
